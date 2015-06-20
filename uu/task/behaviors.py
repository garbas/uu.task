from plone.autoform.interfaces import IFormFieldProvider
from plone.supermodel import model
from zope import schema
from zope.interface import alsoProvides


class IAssignedTask(model.Schema):
    """Due Date"""

    due_on = schema.Datetime(title=u"Due Date")


class ITaskRules(model.Schema):
    """Computed Due Date Rules"""

    due_in = schema.Int()
#    due_units = schema.Choice()
#    due_rel = schema.Choice()
#    source = schema.Choice()
    use_dow = schema.Bool(title=u"Select relative to day of the week")
    dow_n = schema.Int()
#    dow = schema.Choice()
    time_due = schema.Time(title=u"Time of day")
#    notification_rules = schema.List()
#    timezone = schema.Choice()


alsoProvides(IAssignedTask, IFormFieldProvider)
alsoProvides(ITaskRules, IFormFieldProvider)