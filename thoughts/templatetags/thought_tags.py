from django import template

from thoughts import repository as thought_repository

register = template.Library()

@register.inclusion_tag('thoughts/index.html')
def show_unlocked_thoughts():
  return {'thoughts': thought_repository.get_thoughts(is_locked=False)}
