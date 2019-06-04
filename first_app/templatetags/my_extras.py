from django import template

register = template.Library()

# use decorator or the latter
@register.filter(name='cut')
def cut(value, arg):
  """
    Cut out all instances of arg from the string
  """
  return value.replace(arg, '')


# register.filter('cut', cut)