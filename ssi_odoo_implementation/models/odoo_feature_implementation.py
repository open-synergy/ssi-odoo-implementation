# Copyright 2022 OpenSynergy Indonesia
# Copyright 2022 PT. Simetri Sinergi Indonesia
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).

from odoo import api, fields, models


class OdooFeatureImplementation(models.Model):
    _name = "odoo_feature_implementation"
    _inherit = [
        "mixin.transaction_confirm",
        "mixin.transaction_open",
        "mixin.transaction_cancel",
    ]
    _description = "Odoo Feature Implementation"
    _approval_from_state = "draft"
    _approval_to_state = "open"
    _approval_state = "confirm"
    _after_approved_method = "action_open"

    # Attributes related to add element on view automatically
    _automatically_insert_view_element = True

    # Attributes related to add element on form view automatically
    _automatically_insert_open_policy_fields = False
    _automatically_insert_open_button = False

    _statusbar_visible_label = "draft,confirm,open"

    _policy_field_order = [
        "confirm_ok",
        "approve_ok",
        "reject_ok",
        "restart_approval_ok",
        "cancel_ok",
        "restart_ok",
        "manual_number_ok",
    ]
    _header_button_order = [
        "action_confirm",
        "action_approve_approval",
        "action_reject_approval",
        "%(ssi_transaction_cancel_mixin.base_select_cancel_reason_action)d",
        "action_restart",
    ]

    # Attributes related to add element on search view automatically
    _state_filter_order = [
        "dom_draft",
        "dom_confirm",
        "dom_reject",
        "dom_open",
        "dom_cancel",
    ]

    _create_sequence_state = "open"

    date = fields.Date(
        string="Date",
        required=True,
        readonly=True,
        states={"draft": [("readonly", False)]},
        default=lambda self: self._default_date(),
    )
    implementation_id = fields.Many2one(
        string="# Implementation",
        comodel_name="odoo_implementation",
        ondelete="restrict",
        required=True,
    )
    partner_id = fields.Many2one(
        string="Client",
        comodel_name="res.partner",
        related="implementation_id.partner_id",
        store=True,
    )
    contact_id = fields.Many2one(
        string="Contact",
        comodel_name="res.partner",
    )
    feature_id = fields.Many2one(
        string="Feature",
        comodel_name="odoo_feature",
        ondelete="restrict",
        required=True,
    )
    category_id = fields.Many2one(
        string="Category",
        comodel_name="odoo_feature_category",
        related="feature_id.category_id",
        store=True,
    )
    state = fields.Selection(
        string="State",
        selection=[
            ("draft", "Initial Preparation"),
            ("confirm", "Waiting for Live Approval"),
            ("open", "Running"),
            ("reject", "Reject for Live"),
            ("cancel", "Installed Not Used"),
        ],
        copy=False,
        default="draft",
        required=True,
        readonly=True,
    )

    @api.model
    def _default_date(self):
        return fields.Date.today()

    @api.model
    def _get_policy_field(self):
        res = super(OdooFeatureImplementation, self)._get_policy_field()
        policy_field = [
            "confirm_ok",
            "approve_ok",
            "reject_ok",
            "open_ok",
            "cancel_ok",
            "restart_ok",
            "restart_approval_ok",
            "manual_number_ok",
        ]
        res += policy_field
        return res

    @api.onchange(
        "partner_id",
    )
    def onchange_contact_id(self):
        self.contact_id = False
