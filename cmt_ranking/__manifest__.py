# -*- coding: utf-8 -*-
{
    'name': "Ranking para Cliente",

    'summary': """Asignar Ranking a clientes""",

    'description': """
        Asignar una calificación a los clientes basados en el promedio de ventas por año
    """,

    'author': "soluciones4g",
    'website': "http://www.soluciones4g.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Test',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'sale_crm'],

    # always loaded
    'data': [

        'views/vista_partner.xml',
        'views/vista_ranking.xml',
        'security/ir.model.access.csv',
        'data/data_ranking.xml',
        'views/vista_calendar.xml',
        #'views/vista_reunion.xml',
        #'views/vista_partner_corrigiendo.xml',
        #'views/views.xml',
        # 'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        #'demo/demo_curso.xml',
    ],
    'intallable': True,
    'auto_install': False,
}
