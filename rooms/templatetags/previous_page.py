from django import template

register = template.Library()


@register.filter(name="previous_page")
def previous_page(value):

    split = value.split("&")
    for s in split:
        if "page=" in s:
            page_num = str(int(s.replace("page=", "")) - 1)
            value = value.replace(s, "page=" + page_num)
    return value
