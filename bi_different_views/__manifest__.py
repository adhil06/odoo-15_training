# -*- coding: utf-8 -*-
{
    "name": "bi_different_views",

    "summary": """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.odoo.com""",

    "description": """
        in this module i have created different views-form,list,kanban and add custom filter,group by. then created a email using code and perform schedular action in a field
    """,

    "author": "Bassam Infotech LLP",
    "website": "https://bassaminfotech.com",
    "support": "sales@bassaminfotech.com",
    "license": "OPL-1",
    "category": "Uncategorized",
    "version": "15.0.0.1",
    "depends": ["base","sale","bi_adhil_report"],
    "data": [
        "security/ir.model.access.csv",
        "views/diff_views.xml",
        "views/mail_template.xml",
        "views/schedular_cron.xml"
    ],
}