from django import template

register = template.Library()

@register.filter
def ru_pluralize(value, forms):
    forms = forms.split(',')
    value = abs(int(value))

    if value % 10 == 1 and value % 100 != 11:
        form = forms[0]
    elif 2 <= value % 10 <= 4 and (value % 100 < 10 or value % 100 >= 20):
        form = forms[1]
    else:
        form = forms[2]

    return form
