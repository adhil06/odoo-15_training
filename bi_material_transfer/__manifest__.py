# -*- coding: utf-8 -*-
{
    "name": "bi_material_transfer",

    "summary": """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.odoo.com""",

    "description": """
        This module is used for material transfer 
    """,

    "author": "Bassam Infotech LLP",
    "website": "https://bassaminfotech.com",
    "support": "sales@bassaminfotech.com",
    "license": "OPL-1",
    "category": "Uncategorized",
    "version": "15.0.0.1",
    "depends": ["base","stock","product"],
    "data": [
        "security/ir.model.access.csv",
        "views/material_transfer.xml",
    ],
}