from django import template

register = template.Library()

def currency(value):
  return '${0}'.format(value)

register.filter('currency', currency)
