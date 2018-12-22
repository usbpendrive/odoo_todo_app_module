from odoo.exceptions import AccessError
from odoo.tests.common import TransactionCase


class TestTodo(TransactionCase):
    def setUp(self, *args, **kwargs):
        result = super(TestTodo, self).setUp(*args, **kwargs)
        user_demo = self.env.ref('base.user_demo')
        self.env = self.env(user=user_demo)
        return result

    def test_create(self):
        """Create a simple Todo"""
        Todo = self.env['todo.task']
        task = Todo.create({'name': 'Test Task'})
        self.assertEqual(task.is_done, False)

    def test_clear_done(self):
        """Clear Done sets to non active"""
        Todo = self.env['todo.task']
        task = Todo.create({'name': 'Test Task'})
        task.do_clear_done()
        self.assertFalse(task.active)

    def test_record_rule(self):
        """Test per User record rules"""
        Todo = self.env['todo.task']
        task = Todo.sudo().create({'name': 'Admin Task'})
        with self.assertRaises(AccessError):
            Todo.browse([task.id]).name
