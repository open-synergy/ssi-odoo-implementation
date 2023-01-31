# Copyright 2023 OpenSynergy Indonesia
# Copyright 2023 PT. Simetri Sinergi Indonesia
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).

from odoo import fields, models


class OdooModule(models.Model):
    _name = "odoo_module"
    _inherit = ["mixin.master_data"]
    _description = "Odoo Module"

    repository_id = fields.Many2one(
        string="Repository",
        comodel_name="odoo_repository",
        required=True,
    )
    odoo_version_ids = fields.Many2many(
        string="Odoo Versions",
        comodel_name="odoo_version",
        relation="rel_module_2_version",
        column1="module_id",
        column2="odoo_version_id",
        required=True,
    )
