# Copyright 2022 OpenSynergy Indonesia
# Copyright 2022 PT. Simetri Sinergi Indonesia
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).

{
    "name": "Odoo Implementation",
    "version": "14.0.2.0.0",
    "website": "https://simetri-sinergi.id",
    "author": "OpenSynergy Indonesia, PT. Simetri Sinergi Indonesia",
    "license": "LGPL-3",
    "installable": True,
    "application": True,
    "depends": [
        "ssi_master_data_mixin",
        "ssi_transaction_confirm_mixin",
        "ssi_transaction_open_mixin",
        "ssi_transaction_done_mixin",
        "ssi_transaction_terminate_mixin",
        "ssi_transaction_cancel_mixin",
    ],
    "data": [
        "security/ir_module_category_data.xml",
        "security/res_group_data.xml",
        "security/ir.model.access.csv",
        "menu.xml",
        "data/ir_sequence_data.xml",
        "data/sequence_template_data.xml",
        "data/policy_template_data.xml",
        "data/approval_template_data.xml",
        "views/odoo_version_views.xml",
        "views/odoo_feature_views.xml",
        "views/odoo_feature_category_views.xml",
        "views/odoo_environment_views.xml",
        "views/odoo_implementation_views.xml",
        "views/odoo_feature_implementation_views.xml",
        "views/odoo_repository_views.xml",
        "views/odoo_module_views.xml",
        "views/odoo_technical_requirement_views.xml",
        "wizards/wizard_generate_repo_views.xml",
        "wizards/wizard_generate_module_views.xml",
    ],
    "demo": [],
    "external_dependencies": {
        "python": ["GitPython", "pygount", "pathspec", "PyGithub"]
    },
}
