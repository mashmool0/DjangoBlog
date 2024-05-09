from django.template import Library

register = Library()


@register.inclusion_tag('account/result.html')
def show_result(text):
    return {text: "text"}
