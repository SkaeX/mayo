from django import template
from ..models import Prequest

register = template.Library()


@register.simple_tag()
def pending_prequest_count():
    return Prequest.objects.filter(pending=True).count()
