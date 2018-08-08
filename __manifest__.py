# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.


{
    'name': 'BCA Bank Statement',
    'version': '0.1',
    'category': 'Accounting',
    'sequence': 1,
    'summary': 'Get BCA Bank Statement',
    'description': """

==================================================


       """,
    'website': 'https://www.falinwa.com/web/bca_statement',
    'depends': ['base', 'account'],
    'data': [
        'data/bca_data.xml'
        # 'views/bca_bank_statement.xml',
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
