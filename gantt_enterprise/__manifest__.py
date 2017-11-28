# -*- coding: utf-8 -*-
{
    'name': "Vista Gantt en Proyectos",

    'summary': """Agregar vista Gantt a proyectos""",

    'description': """
       Agregar vista gantt al modelo de proyectos basado en el tiempo inicial y final de las tareas
    """,

    'author': "soluciones4g",
    'website': "http://www.soluciones4g.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Test',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'project','web_gantt'],

    # always loaded
    'data': [

        'views/vistas_tareas.xml',
        
    ],
    # only loaded in demonstration mode
    'demo': [
        #'demo/demo_curso.xml',
    ],
    'intallable': True,
    'auto_install': False,
}
