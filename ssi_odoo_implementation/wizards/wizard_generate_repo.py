# Copyright 2023 OpenSynergy Indonesia
# Copyright 2023 PT. Simetri Sinergi Indonesia
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).

from github import Github
from github.GithubException import UnknownObjectException

from odoo import _, fields, models, tools
from odoo.exceptions import Warning as UserError


class WizardGenerateRepo(models.TransientModel):
    _name = "wizard.generate_repo"
    _description = "Wizard Get List Repository"

    name = fields.Char(string="Organization Name", required=True)

    def generate(self):
        for document in self:
            document._generate(document.name)

    def _generate(self, name):
        self.ensure_one()
        github_obj = self.get_github_connector()

        try:
            repos = github_obj.get_organization(name).get_repos()
        except UnknownObjectException:
            raise UserError(_("Invalid name '%s' provided" % name))
        except BaseException as err:
            raise UserError(_("%s" % err))

        if repos:
            self._create_odoo_repository(repos)
        return True

    def _prepare_repo_data(self, repo):
        self.ensure_one()
        return {
            "code": repo.id,
            "name": repo.name,
            "full_name": repo.full_name,
            "html_url": repo.html_url,
        }

    def _check_repository(self, name):
        result = False
        check = self.env["odoo_repository"].search([("name", "=", name)])
        if check:
            result = True
        return result

    def _create_odoo_repository(self, repos):
        self.ensure_one()
        OdooRepo = self.env["odoo_repository"]
        for repo in repos:
            # check = self._check_repository(repo.name)
            # if not check:
            OdooRepo.create(self._prepare_repo_data(repo))

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
