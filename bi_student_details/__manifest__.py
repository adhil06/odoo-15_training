# -*- coding: utf-8 -*-
{
    "name": "Student Detail",
    "description": """
        This module is used for storing student details in student_details table
    """,

    "author": "Bassam Infotech LLP",
    "website": "https://bassaminfotech.com",
    "support": "sales@bassaminfotech.com",
    "license": "OPL-1",
    "category": "Uncategorized",
    "version": "15.0.0.1",
    "depends": ["base","sale"],
    "data": [
        "security/ir.model.access.csv",
        "views/student_details.xml",
        "views/subject_details.xml",
    ],
}