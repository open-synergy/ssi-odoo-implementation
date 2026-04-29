# Copyright 2025 OpenSynergy Indonesia
# Copyright 2025 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
#
# Migration: 14.0.1.0.0 -> 14.0.1.1.0
#
# Changes: data_requirement_ids on odoo_deployment, odoo_implementation, and
#          odoo_feature_issue were Many2many fields with auto-generated junction
#          table names. Migrate any existing rows into data_requirement.document
#          (table: data_requirement_document).
#
# Auto-generated table names (Odoo 14 alphabetical convention):
#   odoo_deployment      -> data_requirement_odoo_deployment_rel
#   odoo_implementation  -> data_requirement_odoo_implementation_rel
#   odoo_feature_issue   -> data_requirement_odoo_feature_issue_rel

import logging

from openupgradelib import openupgrade

_logger = logging.getLogger(__name__)

# (old_junction_table, column_with_res_id, res_model)
_JUNCTION_TABLES = [
    (
        "data_requirement_odoo_deployment_rel",
        "odoo_deployment_id",
        "odoo_deployment",
    ),
    (
        "data_requirement_odoo_implementation_rel",
        "odoo_implementation_id",
        "odoo_implementation",
    ),
    (
        "data_requirement_odoo_feature_issue_rel",
        "odoo_feature_issue_id",
        "odoo_feature_issue",
    ),
]


def _migrate_junction_table(cr, table, res_id_col, res_model):
    openupgrade.logged_query(
        cr,
        """
        SELECT 1 FROM information_schema.tables
        WHERE table_schema = 'public'
          AND table_name = %s
        """,
        (table,),
    )
    if not cr.fetchone():
        _logger.info("Table %s does not exist, skipping.", table)
        return

    openupgrade.logged_query(
        cr,
        f"""
        INSERT INTO data_requirement_document (res_model, res_id, data_requirement_id)
        SELECT %s, {res_id_col}, data_requirement_id
        FROM {table}
        ON CONFLICT DO NOTHING
        """,
        (res_model,),
    )
    _logger.info("Migrated rows from %s into data_requirement_document.", table)


@openupgrade.migrate()
def migrate(env, version):
    for table, col, model in _JUNCTION_TABLES:
        _migrate_junction_table(env.cr, table, col, model)
