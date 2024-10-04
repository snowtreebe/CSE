# -*- coding: utf-8 -*-
{
    'name': "Field Service Reports",
    'version': '17.0.0.0.0',
    'category': 'Service',
    'author': 'Morena Sandroni',
    "license": "LGPL-3",
    'description': """
        This module add/modify 2 reports for Field Service.
    """,
    'depends': [
        'base',
        'industry_fsm_report',
    ],
    'data': [
        'reports/report_service_task.xml',
        'reports/worksheet_custom_page_report.xml',
        'views/worksheet_custom_page.xml',
    ],

    'installable' : True,
    'application' : False,
}

