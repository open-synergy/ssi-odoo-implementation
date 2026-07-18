# Copyright 2026 OpenSynergy Indonesia
# Copyright 2026 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import models


class OdooImplementation(models.Model):  # pylint: disable=too-few-public-methods
    _name = "odoo_implementation"
    _inherit = [
        "odoo_implementation",
        "mixin.single_operating_unit",
    ]
