from django.template import Library, Node
from django.template.defaultfilters import stringfilter
import settings

import re
register = Library()

@register.inclusion_tag('codewiki/templatetags/screenshot.html')
def screen_shot(code_object, size='medium'):
    
    if code_object.has_screenshot(size=size):
        url = settings.MEDIA_URL + 'screenshots/medium/' + code_object.get_screenshot_filename(size=size)
    else:
        url = settings.MEDIA_URL + 'images/testcard_' + size + '.png'
    print url
    return {
        'url': url,
        'title': code_object.title,    
    }

