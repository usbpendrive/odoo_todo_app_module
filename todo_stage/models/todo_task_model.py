from odoo import api, fields, models
from odoo.exceptions import ValidationError
from odoo.addons.base.res.res_request import referenceable_models


class TodoTask(models.Model):
    _name = 'todo.task'
    _inherit = ['todo.task', 'mail.thread']

    effort_estimate = fields.Integer()
    name = fields.Char(help="What needs to be done?")

    stage_id = fields.Many2one('todo.task.stage', 'Stage')
    tag_ids = fields.Many2many(
        'todo.task.tag',
        'todo_task_tag_rel',
        'task_id',
        'tag_id',
        string='Tags',
        auto_join=False,
        context={},
        domain=[],
        ondelete='cascade')

    refers_to = fields.Reference(
        referenceable_models, 'Refers to')
    state = fields.Selection(related='stage_id.state', string='Stage State', store=True)

    stage_fold = fields.Boolean(
        string='Stage Folded?',
        compute='_compute_stage_fold',
        search='_search_stage_fold',
        inverse='_write_stage_fold',
        store=False
    )

    @api.depends('stage_id.fold')
    def _compute_stage_fold(self):
        for todo in self:
            todo.stage_fold = todo.stage_id.fold

    @staticmethod
    def _search_stage_fold(operator, value):
        return [('stage_id.fold', operator, value)]

    def _write_stage_fold(self):
        for todo in self:
            todo.stage_id.fold = todo.stage_fold

    _sql_constraints = [(
        'todo_task_name_unique',
        'UNIQUE (name, active)',
        'Task title must be unique!'
    )]

    @api.constrains('name')
    def _check_name_size(self):
        for todo in self:
            if len(todo.name) < 5:
                raise ValidationError('Title must have 5 chars')

    @api.onchange('user_id')
    def onchange_user_id(self):
        if not self.user_id:
            self.team_ids = None
            return {
                'warning': {
                    'title': 'Responsible User Reset',
                    'message': 'Please choose a new team'
                }
            }

    @api.model
    def create(self, vals):
        new_record = super(TodoTask, self).create(vals)
        return new_record

    @api.multi
    def write(self, vals):
        super(TodoTask, self).write(vals)
        return True

    def _compute_user_todo_count(self):
        for task in self:
            task.user_todo_count = task.search_count([('user_id', '=', task.user_id.id)])

    user_todo_count = fields.Integer('User To-Do Count', compute='_compute_user_todo_count')

    color = fields.Integer('Color Index')
    priority = fields.Selection(
        [('0', 'Low'),
         ('1', 'Normal'),
         ('2', 'High')],
        'Priority',
        default='1')
    kanban_state = fields.Selection(
        [('normal', 'In Progress'),
         ('blocked', 'Blocked'),
         ('done', 'Ready for next stage')],
        'Kanban State',
        default='normal')
