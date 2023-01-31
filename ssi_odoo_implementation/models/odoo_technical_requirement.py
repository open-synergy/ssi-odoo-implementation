# Copyright 2023 OpenSynergy Indonesia
# Copyright 2023 PT. Simetri Sinergi Indonesia
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).

from odoo import api, fields, models


class OdooTechnicalRequirement(models.Model):
    _name = "odoo_technical_requirement"
    _inherit = ["mixin.master_data"]
    _description = "Odoo Technical Requirement"

    repository_id = fields.Many2one(
        string="Repository",
        comodel_name="odoo_repository",
        required=True,
    )

    @api.depends(
        "repository_id",
    )
    def _compute_allowed_module_ids(self):
        for document in self:
            result = []
            if document.repository_id:
                module_ids = self.env["odoo_module"].search(
                    [("repository_id", "=", document.repository_id.id)]
                )
                if module_ids:
                    result = module_ids.ids
            document.allowed_module_ids = result

    allowed_module_ids = fields.Many2many(
        string="Allowed Modules",
        comodel_name="odoo_module",
        compute="_compute_allowed_module_ids",
        store=False,
    )
    module_id = fields.Many2one(
        string="Module",
        comodel_name="odoo_module",
        required=True,
    )
    module_version = fields.Char(
        string="Module Version",
        required=True,
    )

    @api.depends(
        "module_id",
    )
    def _compute_allowed_odoo_version_id(self):
        for document in self:
            result = []
            if document.module_id:
                version_ids = document.module_id.mapped("odoo_version_ids")
                if version_ids:
                    result = version_ids.ids
            document.allowed_odoo_version_ids = result

    allowed_odoo_version_ids = fields.Many2many(
        string="Allowed Odoo Version",
        comodel_name="odoo_version",
        compute="_compute_allowed_odoo_version_id",
        store=False,
    )
    odoo_version_id = fields.Many2one(
        string="Module Version",
        comodel_name="odoo_version",
        required=True,
    )
    dependency_ids = fields.Many2many(
        string="Depends",
        comodel_name="odoo_module",
        relation="rel_technical_2_module_dependencies",
        column1="requirement_id",
        column2="module_id",
    )
