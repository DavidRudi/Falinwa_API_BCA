# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.


{
    'name': 'Bank Api',
    'version': '0.1',
    'category': 'Accounting',
    'sequence': 1,
    'summary': 'Import Bank Statement from API',
    'description': """

==================================================


       """,
    'website': 'https://www.falinwa.com/web/bank_api',
    'depends': ['base', 'account'],
    'data': [
        # 'data/bank_api_data.xml',
        'views/bank_api.xml',
        'views/account_journal_bank_api.xml',
        'wizard/bank_api_wizard.xml',
    ],
    'demo': [
        'demo/demo.xml'
    ],
    'installable': True,
    'auto_install': False,
    # 'qweb': [
    #     "static/src/xml/attendance.xml",
    # ],
    'application': True,
}
