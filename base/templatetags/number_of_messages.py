
from django import template
from ..models import UserMessage

register = template.Library()

@register.filter
def total_messages(user_id):
    messages = UserMessage.objects.filter()
    return len(messages)
