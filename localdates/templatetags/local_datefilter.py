from django.template import resolve_variable, Library
from django.conf import settings
from django.utils.translation import gettext, ngettext, get_language

register = Library()

from django.contrib.localdates.local_dateformat import format, time_format

###################
# DATES           #
###################

def ldate(value, arg=None):
    "Formats a date according to the given format"
    if not value:
        return ''
    if arg is None:
        arg = settings.DATE_FORMAT
    return format(value, arg, get_language())


def ltime(value, arg=None):
    "Formats a time according to the given format"   
    if value in (None, ''):
        return ''
    if arg is None:
        arg = settings.TIME_FORMAT
    return time_format(value, arg, get_language())

# below here nothing works
def ltimesince(value, arg=None):
    'Formats a date as the time since that date (i.e. "4 days, 6 hours")'
    from django.utils.timesince import timesince
    if not value:
        return ''
    if arg:
        return timesince(arg, value)
    return timesince(value)

def ltimeuntil(value, arg=None):
    'Formats a date as the time until that date (i.e. "4 days, 6 hours")'
    from django.utils.timesince import timesince
    from datetime import datetime
    if not value:
        return ''
    if arg:
        return timesince(arg, value)
    return timesince(datetime.now(), value)
    
register.filter(ldate)
register.filter(ltime)
register.filter(ltimesince)
register.filter(ltimeuntil)
