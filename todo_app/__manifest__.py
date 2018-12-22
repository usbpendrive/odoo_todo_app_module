{
    'name': 'To-Do app',
    'description': 'Manage personal to-do tasks',
    'author': 'Fernando',
    'license': 'LGPL-3',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'security/todo_access_rules.xml',
        'views/todo_menu.xml',
        'views/todo_views.xml',
        'views/res_partner_view.xml',
        'views/index_template.xml',
    ],
    'application': True
}
