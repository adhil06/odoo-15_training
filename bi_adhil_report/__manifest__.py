# -*- coding: utf-8 -*-
{
    "name": "bi_adhil_report",

    "summary": """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.odoo.com""",

    "description": """
        Long description of module's purpose
    """,

    "author": "Bassam Infotech LLP",
    "website": "https://bassaminfotech.com",
    "support": "sales@bassaminfotech.com",
    "license": "OPL-1",
    "category": "Uncategorized",
    "version": "0.1",
    "depends": ["sale"],
    "data": [
        # "security/ir.model.access.csv",
        # "views/views.xml",
        # "reports/car_company.xml",
        "reports/sale_card.xml",
        "reports/report.xml",
    ],
}