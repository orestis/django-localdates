

from django.utils.dateformat import TimeFormat, DateFormat
import re


local_re = re.compile(r'(\{\w{2}\})')



standard_format_strings = {
    'FULL_DATE':'l, j {Fp}, Y',
    'ABBR_DATE':'j M, Y',
    'NUM_DATE':'j/n/Y',
    #fix this
    'FULL_DATETIME':'l, j {Fp}, Y, P',
    'ABBR_DATETIME':'j M, Y, P',
    'NUM_DATETIME':'j/n/Y, P',
    
    'FULL_TIME':'P',
    'FULL_YEARMONTH':'F Y',
    'ABBR_YEARMONTH':'M Y',
    'NUM_YEARMONTH':'n/Y',
    'FULL_MONTHDAY':'j {Fp}',
    'ABBR_MONTHDAY':'j M',
    'NUM_MONTHDAY':'j/n',

}

#this construcs the regexp string like this: r"(\{FULL_DATE\}|\{ABBR_DATE\}|...)"
local_standard_string = r'('+(r'|'.join([r'\{%s\}'%key for key in standard_format_strings]))+r')'

local_standard_re = re.compile(local_standard_string)

class LocalFormatter(object):
    def format(self, formatstr):
    
        #formatstr = unicode(formatstr)
        # replace the standard strings with their expanded versions
        standard_pieces = local_standard_re.findall(formatstr)
        for piece in standard_pieces:
            formatstr = formatstr.replace(piece, standard_format_strings[piece[1:-1]])
        
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


class LocalDateFormat(LocalFormatter, DateFormat):
    def __init__(self, *args, **kwargs):
        self._format = DateFormat.format
        super(DateFormat, self).__init__(*args, **kwargs)
    
    
#    def Fp(self):
#        return MONTHS_POS[self.data.month]
        
    
    
def format(value, format_string, locale=None):
    "Convenience function"
    if locale == None:
        df = DateFormat(value)
    else:
        # try to import the dateformat from the localflavor
        
        try:
            localflavor_module = __import__('django.contrib.localflavor.%s.dateformat'%locale[:2], {}, {}, [''])
            #print localflavor_module
            df_class = getattr(localflavor_module, 'LocalDateFormat')
            #print df_class
            df = df_class(value)
        except (ImportError, AttributeError), e:
            #print 'could not import localflavor module', e
            # for now, we just use the custom LocalDateFormat described above
            df = LocalDateFormat(value)
        

        
    return df.format(format_string)

def time_format(value, format_string):
    "Convenience function"
    tf = TimeFormat(value)
    return tf.format(format_string)