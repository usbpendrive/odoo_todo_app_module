from odoo import http
from odoo.http import request


class Todo(http.Controller):
    @http.route('/helloworld', auth='public')
    def hello_world(self):
        """
        Basic Hello World Example
        :return:
        """
        return '<h1>Hello World!</h1>'

    @http.route('/hello', auth='public')
    def hello(self, **kwargs):
        """
        Hello World using a Qweb Template
        Also used for the controller extension example
        :param kwargs:
        :return:
        """
        return request.render('todo_website.hello')

    @http.route('/hellocms/<page>', auth='public')
    def hellocms(self, page, **kwargs):
        """
        Very simple cms page
        :param page:
        :param kwargs:
        :return:
        """
        return request.render(page)

    @http.route('/todos', auth='user', website=True)
    def index(self, **kwargs):
        """
        ToDo List Page
        :param kwargs:
        :return:
        """
        TodoTask = request.env['todo.task']
        tasks = TodoTask.search([])
        return request.render('todo_website.index', {'tasks': tasks})

    @http.route('/todo/<model("todo.task"):task>', website=True)
    def detail(self, task, **kwargs):
        """
        Todo Detail page
        :param task:
        :param kwargs:
        :return:
        """
        return request.render('todo_website.detail', {'task': task})

    @http.route('/todo/add', website=True)
    def add(self, **kwargs):
        """
        Form to add a new Todo Task
        :param kwargs:
        :return:
        """
        users = request.env['res.users'].search([])
        return request.render('todo_website.add', {'users': users})
