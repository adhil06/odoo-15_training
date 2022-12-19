# -*- coding: utf-8 -*-
{
    "name": "Sale Excel Report",
    "description": """
        Excel report for sales
    """,
    "author": "Bassam Infotech LLP",
    "website": "https://bassaminfotech.com",
    "support": "sales@bassaminfotech.com",
    "license": "OPL-1",
    "category": "Sales",
    "version": "15.0.0.1",
    "depends": ["sale"],    
    "data": [
        "security/ir.model.access.csv",
        "wizard/sale_excel_report_wizard.xml",
    ],
}