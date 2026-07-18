.. image:: https://img.shields.io/badge/licence-AGPL--3-blue.svg
   :target: http://www.gnu.org/licenses/agpl-3.0-standalone.html
   :alt: License: AGPL-3

====================================
Odoo Implementation + Operating Unit
====================================

Glue module that adds Operating Unit support to the Odoo Implementation module.
Extends ``odoo_configuration_change_record``, ``odoo_change_request``,
``odoo_feature_issue``, ``odoo_feature_implementation``, ``odoo_deployment``,
``odoo_implementation``, and ``odoo_use_case_specification`` with
``mixin.single_operating_unit``, so that Odoo Implementation transaction data
can be scoped and restricted per operating unit.


Bug Tracker
===========

Bugs are tracked on `GitHub Issues <https://github.com/open-synergy/ssi-odoo-implementation/issues>`_.
In case of trouble, please check there if your issue has already been reported.


Credits
=======

Contributors
------------

* Andhitia Rama <andhitia.r@gmail.com>

Maintainer
----------

.. image:: https://simetri-sinergi.id/logo.png
   :alt: PT. Simetri Sinergi Indonesia
   :target: https://simetri-sinergi.id

This module is maintained by the PT. Simetri Sinergi Indonesia.
