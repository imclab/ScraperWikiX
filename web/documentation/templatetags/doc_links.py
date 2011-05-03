#!/usr/bin/env python

from django import template
register = template.Library()

from documentation.titles import page_titles

@register.simple_tag
def doc_link_full(template_name, language):
    template_name = template_name.replace('LANG', language)
    title = page_titles[template_name][0]
    return '''<a href="/docs/%s/%s">%s</a>''' % (language, template_name, title)


