# -*- coding: utf-8 -*-
{
    'name': "Users Management",

    'summary': """
        A module for the ServerApplication-Reto2 users data management.
    """,

    'description': """
        A module for the ServerApplication-Reto2 users data management.
        It will manage the premium user autorrenovation, the ammount of months
        the user's been premium, the rating average for a users document and
        how many times they've been downloaded.
    """,

    'author': "2DAM2Curious",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/10.0/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'views/userForm.xml',
        'views/documentForm.xml',
        'views/groupForm.xml',
        'views/documentsReport.xml',
        'views/premiumReport.xml',
        'views/groupReport.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}