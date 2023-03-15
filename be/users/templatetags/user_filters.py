from django import template
from django.contrib.auth.models import Group

register = template.Library()

@register.filter(name='is_judge_or_superuser')
def is_judge_or_superuser(user):
    return user.is_superuser or user.groups.filter(name='Judges').exists()
