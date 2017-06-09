from django import template

register=template.Library()

def element(bar,value):
    return bar[value]

register.filter("element",element)
