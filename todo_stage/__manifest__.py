{
    'name': 'Add Stages and Tags to To-Dos',
    'author': 'Fernando',
    'license': 'LGPL-3',
    'depends': ['todo_app', 'mail'],
    'data': [
        'security/ir.model.access.csv',
        'views/todo_menu.xml',
        'views/todo_view.xml',
        'views/todo_kanban_assets.xml',
        'views/todo_kanban_view.xml',
        'reports/todo_report.xml',
        'reports/todo_task_report.xml',
    ],
    'demo': [
        'data/todo.task.csv',
        'data/todo_task.xml',
    ]
}
