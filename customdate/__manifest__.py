# -*- coding: utf-8 -*-
{
    'name': "customdate",

    'summary': """
        Aplicación que permite hacer la conversión del campo Próxima recurrencia del tipo Fecha al tipo Fecha y Hora (datetime)""",

    'description': """
        Aplicación que permite hacer la conversión del campo Próxima recurrencia del tipo Fecha al tipo Fecha y Hora (datetime)
    """,

    'author': "SEDITEC",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['industry_fsm', 'project'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
