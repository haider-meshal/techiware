# -*- coding: utf-8 -*-
{
    'name': "TODO",

    'summary': """
       Todo personal Tasks
    """,

    'description': """
       This is a first module in odoo
    """,

    'author': "Techiware",
    'website': "http://www.Techiware.com",
    'category': 'Productivity',
    'version': '0.1',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'security/todo_access_rules.xml',
        'views/todo_view.xml',
        'views/todo_menu.xml',
        'views/res_partner_view.xml',
        'views/index_template.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
