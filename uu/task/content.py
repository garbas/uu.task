from .interfaces import ITask
from .interfaces import ITaskPlanner
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from plone.dexterity.browser import add
from plone.dexterity.browser import edit
from plone.supermodel import model
from zope.interface import implementer


class TaskAddForm(add.DefaultAddForm):
    """Custom add form for Task
    """


class TaskEditForm(edit.DefaultEditForm):
    """Custom edit form for Task
    """
    template = ViewPageTemplateFile('templates/task_edit.pt')


class TaskPlannerAddForm(add.DefaultAddForm):
    """Custom add form for Task Planner
    """


class TaskPlannerEditForm(edit.DefaultEditForm):
    """Custom edit form for Task
    """
    template = ViewPageTemplateFile('templates/taskplanner_edit.pt')


@implementer(ITask)
class Task(model.Schema):
    """Assignable task with due date
    """


@implementer(ITaskPlanner)
class TaskPlanner(model.Schema):
    """Series of tasks with shared settings
    """
