# Copyright 2022 OpenSynergy Indonesia
# Copyright 2022 PT. Simetri Sinergi Indonesia
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).

from odoo import api, fields, models


class OdooFeatureImplementation(models.Model):
    _name = "odoo_feature_implementation"
    _inherit = [
        "odoo_feature_implementation",
    ]

    project_id = fields.Many2one(
        string="Project",
        related="implementation_id.project_id",
    )
    task_ids = fields.Many2many(
        string="Direct Tasks",
        comodel_name="project.task",
        relation="rel_feature_implementation_2_direct_task",
        column1="feature_implementation_id",
        column2="task_id",
    )
    num_direct_task = fields.Integer(
        string="Number of Direct Tasks",
        compute="_compute_num_direct_task",
        store=True,
    )
    num_direct_draft_task = fields.Integer(
        string="Number of Draft Direct Tasks",
        compute="_compute_num_direct_task",
        store=True,
    )
    num_direct_open_task = fields.Integer(
        string="Number of Open Direct Tasks",
        compute="_compute_num_direct_task",
        store=True,
    )
    num_direct_done_task = fields.Integer(
        string="Number of Done Direct Tasks",
        compute="_compute_num_direct_task",
        store=True,
    )
    num_direct_cancel_task = fields.Integer(
        string="Number of Draft Direct Tasks",
        compute="_compute_num_direct_task",
        store=True,
    )
    num_direct_pending_task = fields.Integer(
        string="Number of Draft Direct Tasks",
        compute="_compute_num_direct_task",
        store=True,
    )

    @api.depends(
        "task_ids",
        "task_ids.stage_id",
    )
    def _compute_num_direct_task(self):
        for record in self:
            total = (
                total_draft
            ) = total_open = total_done = total_pending = total_cancel = 0
            for task in record.task_ids:
                total += 1
                if task.state == "draft":
                    total_draft += 1
                elif task.state == "open":
                    total_open += 1
                elif task.state == "done":
                    total_done += 1
                elif task.state == "pending":
                    total_pending += 1
                elif task.state == "cancelled":
                    total_cancel += 1
            record.num_direct_task = total
            record.num_direct_draft_task = total_draft
            record.num_direct_open_task = total_open
            record.num_direct_done_task = total_done
            record.num_direct_cancel_task = total_cancel
            record.num_direct_pending_task = total_pending
