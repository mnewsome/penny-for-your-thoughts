from django import template

from thoughts.models import Thought

register = template.Library()

@register.inclusion_tag('thoughts/index.html')
def show_thoughts():
  thoughts = Thought.objects.all().order_by('date_created')
  return {'thoughts': thoughts}
