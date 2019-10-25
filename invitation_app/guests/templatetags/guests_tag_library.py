from django import template
register = template.Library()

@register.filter
def format_phone_number(value):
    new_value = str(value)
    return "0" + new_value[0:2] + " " + new_value[2:5] + " " + new_value[5:]