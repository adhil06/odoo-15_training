# -*- coding: utf-8 -*-
{
    "name": "bi_blocking_sale_order",

    "summary": """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.odoo.com""",

    "description": """
       Blooking sale order on the basis of no of days given in settings 
    """,

    "author": "Bassam Infotech LLP",
    "website": "https://bassaminfotech.com",
    "support": "sales@bassaminfotech.com",
    "license": "OPL-1",
    "category": "Uncategorized",
    "version": "15.0.0.1",
    "depends": ["base","sale"],
    "data": [
        # "security/ir.model.access.csv",
        "views/settings.xml",
        "views/sale_order_inher.xml"
    ],
}