from odoo import fields, models


class Tag(models.Model):
    _name = 'todo.task.tag'
    _description = 'To-do Tag'

    name = fields.Char('Name', translate=True)

    task_ids = fields.Many2many('todo.task', string='Tasks')

    _parent_store = True
    _parent_name = 'parent_id'
    parent_id = fields.Many2one(
        'todo.task.tag',
        'Parent Tag',
        ondelete='restrict')
    parent_left = fields.Integer('Parent Left', index=True)
    parent_right = fields.Integer('Parent Right', index=True)
    child_ids = fields.One2many(
        'todo.task.tag',
        'parent_id',
        'Child Tags')
