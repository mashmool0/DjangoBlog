from django import template

register = template.Library()


@register.filter  # you cant set a  name for your def
def cutter(value, arg):
    return value[:arg]

# second method for register
# register.filter('name of your filter',cutter)
