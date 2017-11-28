# -*- coding: utf-8 -*-
{
    'name': "Vista gráficos en Calendarios",

    'summary': """Agregar de gráficos en Calendario""",

    'description': """
       Agregar vista graficos al modelo calendar para monitorear el numero de llamadas
    """,

    'author': "soluciones4g",
    'website': "http://www.soluciones4g.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Test',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'calendar','crm_editado'],

    # always loaded
    'data': [

        'views/vista_calendar_graf.xml',
        'views/vista_calendar_tree.xml',

    ],
    # only loaded in demonstration mode
    'demo': [
        #'demo/demo_curso.xml',
    ],
    'intallable': True,
    'auto_install': False,
}
