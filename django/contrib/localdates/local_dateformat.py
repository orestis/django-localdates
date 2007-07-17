

from django.utils.dateformat import TimeFormat, DateFormat
from django.utils.translation import ugettext as _
import re

local_re = re.compile(r'(\{\w{2}\})')

#to trigger translation    
dummy_formats = (
    _('FULL_DATE'), 
    _('ABBR_DATE'), 
    _('NUM_DATE'), 
   
    _('FULL_DATETIME'), 
    _('ABBR_DATETIME'),
    _('NUM_DATETIME'),
    
    _('FULL_TIME'),
    
    _('FULL_YEARMONTH'),
    _('ABBR_YEARMONTH'),
    _('NUM_YEARMONTH'),
    
    _('FULL_MONTHDAY'),
    _('ABBR_MONTHDAY'),
    _('NUM_MONTHDAY'),
    )

# default to english
default_format_strings = {
    'FULL_DATE':'l, N j, Y',
    'ABBR_DATE':'N j, Y',
    'NUM_DATE':'n/j/Y',

    'FULL_DATETIME':'l, N j, Y, P',
    'ABBR_DATETIME':'N j, Y, P',
    'NUM_DATETIME':'n/j/Y, P',
    
    'FULL_TIME':'P',
    
    'FULL_YEARMONTH':'F Y',
    'ABBR_YEARMONTH':'M Y',
    'NUM_YEARMONTH':'n/Y',
    
    'FULL_MONTHDAY':'F j',
    'ABBR_MONTHDAY':'M j',
    'NUM_MONTHDAY':'n/j',

}


# this is after the django.utils.translation.trans_real.get_date_formats
# TODO take into consideration the settings date formats
def get_local_formats():
    from django.conf import settings
    formats = {}
    
    for format in default_format_strings:
        result = _(format)
        if result == format:
            result = default_format_strings[format]
        formats[format]=result
    
    return formats


#this constructs the regexp string like this: r"(\{FULL_DATE\}|\{ABBR_DATE\}|...)"
local_standard_string = r'('+(r'|'.join([r'\{%s\}'%key for key in get_local_formats()]))+r')'

local_standard_re = re.compile(local_standard_string)

class LocalFormatter(object):
    def format(self, formatstr):
        # replace the standard strings with their expanded versions
        standard_pieces = local_standard_re.findall(formatstr)
        for piece in standard_pieces:
            formatstr = formatstr.replace(piece, get_local_formats()[piece[1:-1]])
        
        # put the local values in the format str
        local_pieces = local_re.findall(formatstr)
        for piece in local_pieces:
            try:
                result = unicode(getattr(self, piece[1:-1])())
                formatstr = formatstr.replace(piece, result)
            except AttributeError:
                # the current local date format doesn't handle this format
                # we don't do anything
                pass
        
        # use the standard behavior for the rest
        return self._format(self, formatstr)


class DefaultLocalDateFormat(LocalFormatter, DateFormat):
    def __init__(self, *args, **kwargs):
        self._format = DateFormat.format
        super(DateFormat, self).__init__(*args, **kwargs)
    
class DefaultLocalTimeFormat(LocalFormatter, TimeFormat):
    def __init__(self, *args, **kwargs):
        self._format = TimeFormat.format
        super(TimeFormat, self).__init__(*args, **kwargs)
    
def _format(value, format_string, locale, format_type='Date'):
    "Convenience function"  
    if locale == None:
        df = DateFormat(value)
    else:
        # try to import the dateformat from the localflavor
        
        try:
            localflavor_module = __import__('django.contrib.localflavor.%s.dateformat'%locale[:2], {}, {}, [''])
            #print localflavor_module
            df_class = getattr(localflavor_module, 'Local%sFormat'%format_type)
            #print df_class
            df = df_class(value)
            
        except (ImportError, AttributeError), e:
            #print 'could not import localflavor module', e
            #use DefaultLocalDateFormat or DefaultLocalTimeFormat
            if format_type=='Date' 
                df = DefaultLocalDateFormat(value)
            elif format_type=='Time'
                df = DefaultLocalTimeFormat(value)
        

        
    return df.format(format_string)

def format(value, format_string, locale=None):
    return _format(value, format_string, locale, 'Date')

def time_format(value, format_string):   
    return _format(value, format_string, locale, 'Time')