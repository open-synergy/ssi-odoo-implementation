# Copyright 2022 OpenSynergy Indonesia
# Copyright 2022 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import models


class OdooEnvironment(models.Model):
    _name = "odoo_environment"
    _inherit = ["mixin.master_data"]
    _description = "Odoo Environment"
