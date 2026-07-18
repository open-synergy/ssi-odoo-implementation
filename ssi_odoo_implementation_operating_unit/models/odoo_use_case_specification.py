# Copyright 2026 OpenSynergy Indonesia
# Copyright 2026 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import models


class OdooUseCaseSpecification(models.Model):  # pylint: disable=too-few-public-methods
    _name = "odoo_use_case_specification"
    _inherit = [
        "odoo_use_case_specification",
        "mixin.single_operating_unit",
    ]
