# Copyright 2023 OpenSynergy Indonesia
# Copyright 2023 PT. Simetri Sinergi Indonesia
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).

from odoo import fields, models


class OdooRepository(models.Model):
    _name = "odoo_repository"
    _inherit = ["mixin.master_data"]
    _description = "Odoo Repository"

    full_name = fields.Char(
        string="Full Name",
    )
    html_url = fields.Char(
        string="URL",
        readonly=False,
        copy=False,
    )
