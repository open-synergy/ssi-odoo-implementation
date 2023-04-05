# Copyright 2022 OpenSynergy Indonesia
# Copyright 2022 PT. Simetri Sinergi Indonesia
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).

from odoo import fields, models


class OdooFeature(models.Model):
    _name = "odoo_feature"
    _inherit = ["mixin.master_data"]
    _description = "Odoo Feature"

    category_id = fields.Many2one(
        string="Category",
        comodel_name="odoo_feature_category",
    )
    ttype = fields.Selection(
        string="Type",
        selection=[
            ("transaction", "Transaction"),
            ("master", "Master Data"),
            ("report", "Report"),
        ],
        required=True,
        default="transaction",
    )
