# Copyright 2022 OpenSynergy Indonesia
# Copyright 2022 PT. Simetri Sinergi Indonesia
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).

from odoo import models


class OdooFeature(models.Model):
    _name = "odoo_feature"
    _inherit = ["mixin.master_data"]
    _description = "Odoo Feature"
