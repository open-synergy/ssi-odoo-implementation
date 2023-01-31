# Copyright 2023 OpenSynergy Indonesia
# Copyright 2023 PT. Simetri Sinergi Indonesia
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).

from github import Github
from github.GithubException import UnknownObjectException

from odoo import _, fields, models, tools
from odoo.exceptions import Warning as UserError


class WizardGenerateModule(models.TransientModel):
    _name = "wizard.generate_module"
    _description = "Wizard Get List Modules"

    repository_id = fields.Many2one(
        string="Repository",
        comodel_name="odoo_repository",
        required=True,
    )
    odoo_version_ids = fields.Many2many(
        string="Odoo Versions",
        comodel_name="odoo_version",
        relation="rel_generate_module_2_version",
        column1="module_id",
        column2="odoo_version_id",
        required=True,
    )

    def generate(self):
        for document in self:
            document._generate(document.repository_id.full_name)

    def _generate(self, name):
        self.ensure_one()
        github_obj = self.get_github_connector()

        try:
            modules = github_obj.get_repo(name)
        except UnknownObjectException:
            raise UserError(_("Invalid name '%s' provided" % name))
        except BaseException as err:
            raise UserError(_("%s" % err))

        if modules:
            self._create_odoo_module(modules)
        return True

    def _prepare_module_data(self, module, version_id):
        self.ensure_one()
        return {
            "code": module.name,
            "name": module.name,
            "repository_id": self.repository_id.id,
            "odoo_version_ids": [(6, 0, [version_id])],
        }

    def _prepare_update_data(self, version_id):
        self.ensure_one()
        return {"odoo_version_ids": [(4, version_id)]}

    def _check_module(self, branch, module):
        # 0. Continue
        # 1. Create Module
        # 2. Update, Tambahkan odoo version
        check = 0

        check_1 = self.env["odoo_module"].search([("name", "=", module)])
        if not check_1:
            check = 1
            return check, False

        check_2 = check_1.mapped("odoo_version_ids").mapped("name")
        if branch not in check_2:
            module = check_1
            check = 2
            return check, module
        return check, False

    def _create_odoo_module(self, modules):
        self.ensure_one()
        OdooModule = self.env["odoo_module"]
        for version in self.odoo_version_ids:
            try:
                branch = modules.get_branch(version.name)
            except UnknownObjectException:
                raise UserError(_("Invalid branch name '%s'" % version.name))
            except BaseException as err:
                raise UserError(_("%s" % err))

            if branch:
                contents = modules.get_contents(path="", ref=branch.name)
                for content in contents:
                    excludes = [".github", "setup"]
                    if content.type == "dir" and content.path not in excludes:
                        check, module = self._check_module(branch.name, content.name)
                        if check == 1:
                            OdooModule.create(
                                self._prepare_module_data(content, version.id)
                            )
                        elif check == 2:
                            module.write(self._prepare_update_data(version.id))
                        else:
                            continue

    def get_github_connector(self):
        ICP = self.env["ir.config_parameter"]
        token = tools.config.get("github_token") or ICP.get_param(
            "github.access_token", default=""
        )
        timeout = tools.config.get("github_timeout") or ICP.get_param(
            "github.timeout", default=15
        )
        if not token:
            raise UserError(
                _(
                    "Please add the 'github_token' in Odoo configuration file"
                    " or as the 'github.access_token' configuration parameter."
                )
            )
        return Github(login_or_token=token, timeout=int(timeout))
