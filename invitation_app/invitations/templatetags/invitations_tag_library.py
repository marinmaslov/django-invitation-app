from django import template
#from invitations.models import Escort
register = template.Library()

@register.filter
def format_phone_number(value):
    new_value = str(value)
    return "0" + new_value[0:2] + " " + new_value[2:5] + " " + new_value[5:]

@register.filter
def first_letter(value):
    return value[:1]

@register.filter
def has_escort(value):
    escorts = Escort.objects.all()
    counter = 0
    for escort in escorts:
        if escort.invitation_id == value:
            counter += 1
    if counter > 0:
        return True
    else:
        return False
