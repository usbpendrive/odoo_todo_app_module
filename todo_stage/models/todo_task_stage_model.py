from odoo import fields, models


class Stage(models.Model):
    _name = 'todo.task.stage'
    _description = 'To-do Stage'
    _order = 'sequence, name'
    _rec_name = 'name'
    _table = 'todo_task_stage'

    name = fields.Char(
        string='Name',
        copy=False,
        default='New',
        groups='base.group_user, base.group_no_one',
        help='The title for the stage',
        index=True,
        readonly=False,
        required=True,
        states={'done': [('readonly', False)]},
        size=40,
        translate=True
    )

    desc = fields.Text('Description')
    state = fields.Selection(
        [('draft', 'New'), ('open', 'Started'), ('done', 'Closed')],
        'State'
    )
    docs = fields.Html('Documentation')

    sequence = fields.Integer('Sequence')
    perc_complete = fields.Float('% Complete', (3, 2))

    date_effective = fields.Date('Effective Date')
    date_created = fields.Datetime('Created Date and Time', default=lambda self: fields.Datetime.now())

    fold = fields.Boolean('Folded?')
    image = fields.Binary('Image')

    task_ids = fields.One2many(
        'todo.task',
        'stage_id',
        'Tasks in this stage'
    )
