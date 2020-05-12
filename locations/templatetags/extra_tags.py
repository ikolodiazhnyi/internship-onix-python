from django import template

register = template.Library()


@register.filter
def short_line(line, symbols_count):
    return line[0:symbols_count] if line else '-'
