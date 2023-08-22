import setuptools

with open('VERSION.txt', 'r') as f:
    version = f.read().strip()

setuptools.setup(
    name="odoo14-addons-open-synergy-ssi-odoo-implementation",
    description="Meta package for open-synergy-ssi-odoo-implementation Odoo addons",
    version=version,
    install_requires=[
        'odoo14-addon-ssi_odoo_implementation',
        'odoo14-addon-ssi_odoo_implementation_git',
        'odoo14-addon-ssi_odoo_implementation_project',
    ],
    classifiers=[
        'Programming Language :: Python',
        'Framework :: Odoo',
        'Framework :: Odoo :: 14.0',
    ]
)
