# -*- coding: utf-8 -*-
{
    "name": "Account Reversal",
    "summary": "Wizard for creating a reversal account move",
    "category": "Accounting & Finance",
    "website": "https://odoo-community.org/",
    "author": "Akretion,"
              "Camptocamp,"
              "ACSONE SA/NV,"
              "Tecnativa,"
              "Odoo Community Association (OCA)",
    "license": "AGPL-3",
    "application": False,
    "installable": True,
    # any module necessary for this one to work correctly
    'depends': ['account'],

    # always loaded
    'data': [
        'wizard/account_move_reverse_view.xml',
        'views/account_move_view.xml',

    ],
}
