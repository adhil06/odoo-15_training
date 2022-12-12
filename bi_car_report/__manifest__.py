# -*- coding: utf-8 -*-
{
    "name": "bi_car_report",

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
    "version": "15.0.0.1",
    "depends": ["sale"],
    "data": [
        "reports/paperformat.xml",
        "reports/car_company.xml",
        "reports/report.xml",
        "reports/card_button.xml",
    ],
}