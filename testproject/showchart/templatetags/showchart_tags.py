from django import template
from ..models import HotEvents
from ..models import Event
from django.db.models.aggregates import Count
from django.utils.html import mark_safe
import re
register = template.Library()
@register.simple_tag
def get_event_list():
    return HotEvents.objects.all()
@register.simple_tag
def get_event_detail():
    return Event.objects.all()