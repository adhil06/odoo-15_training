# -*- coding: utf-8 -*-
{
    "name": "bi_different_views",

    "summary": """
        hospital module """,

    "description": """
        in this module i have created different views-form,list,kanban and add custom filter,group by. then created a email using code and perform schedular action in a field alsco sent mail by suing ir.cron also impletement chatter in the form view.
    """,

    "author": "Bassam Infotech LLP",
    "website": "https://bassaminfotech.com",
    "support": "sales@bassaminfotech.com",
    "license": "OPL-1",
    "category": "Uncategorized",
    "version": "15.0.0.1",
    "depends": ["base","sale","product","bi_adhil_report","mail"],
    "data": [
        "security/ir.model.access.csv",
        "views/diff_views.xml",
        "views/mail_template.xml",
        "views/schedular_cron.xml"
    ],
}