# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

{
    "name": "External Odoo Base Arelux",
    "version": "12.0.1.0.0",
    "author": "Odoo Nodriza Tech (ONT), "
              "Odoo Community Association (OCA)",
    "website": "https://nodrizatech.com/",
    "category": "Tools",
    "license": "AGPL-3",
    "depends": [
        "external_odoo_base",  # https://github.com/OdooNodrizaTech/external_odoo
        "arelux_partner_questionnaire",
        "stock",
        "sale",
        "shipping_expedition"  # https://github.com/OdooNodrizaTech/stock
    ],
    "data": [
        "views/external_source_view.xml",
    ],
    "installable": True
}
