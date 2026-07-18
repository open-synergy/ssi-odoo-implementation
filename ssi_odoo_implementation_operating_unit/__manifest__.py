# Copyright 2026 OpenSynergy Indonesia
# Copyright 2026 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
{
    "name": "Odoo Implementation + Operating Unit",
    "version": "14.0.1.0.0",
    "website": "https://simetri-sinergi.id",
    "author": "OpenSynergy Indonesia, PT. Simetri Sinergi Indonesia",
    "contributors": [
        "Andhitia Rama <andhitia.r@gmail.com>",
    ],
    "license": "AGPL-3",
    "installable": True,
    "depends": [
        "ssi_odoo_implementation",
        "ssi_operating_unit_mixin",
    ],
    "data": [
        "security/res_group/odoo_configuration_change_record.xml",
        "security/res_group/odoo_change_request.xml",
        "security/res_group/odoo_feature_issue.xml",
        "security/res_group/odoo_feature_implementation.xml",
        "security/res_group/odoo_deployment.xml",
        "security/res_group/odoo_implementation.xml",
        "security/res_group/odoo_use_case_specification.xml",
        "security/ir_rule/odoo_configuration_change_record.xml",
        "security/ir_rule/odoo_change_request.xml",
        "security/ir_rule/odoo_feature_issue.xml",
        "security/ir_rule/odoo_feature_implementation.xml",
        "security/ir_rule/odoo_deployment.xml",
        "security/ir_rule/odoo_implementation.xml",
        "security/ir_rule/odoo_use_case_specification.xml",
        "view/odoo_configuration_change_record.xml",
        "view/odoo_change_request.xml",
        "view/odoo_feature_issue.xml",
        "view/odoo_feature_implementation.xml",
        "view/odoo_deployment.xml",
        "view/odoo_implementation.xml",
        "view/odoo_use_case_specification.xml",
    ],
}
