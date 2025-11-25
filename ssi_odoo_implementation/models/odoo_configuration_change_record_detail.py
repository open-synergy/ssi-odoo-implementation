# Copyright 2022 OpenSynergy Indonesia
# Copyright 2022 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import fields, models


class OdooConfigurationChangeRecordDetail(models.Model):
    _name = "odoo_configuration_change_record.detail"
    _description = "Odoo Configuration Change Record Detail"
    _order = "configuration_change_record_id, sequence, id"

    configuration_change_record_id = fields.Many2one(
        comodel_name="odoo_configuration_change_record",
        string="Configuration Change Record",
        required=True,
        ondelete="cascade",
    )
    sequence = fields.Integer(string="Sequence", required=True, default=10)
    audit_log_url = fields.Char(string="Audit Log URL", required=True)
    note = fields.Text(string="Note")
