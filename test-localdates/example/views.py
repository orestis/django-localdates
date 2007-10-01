from django.shortcuts import render_to_response
from django.template.context import RequestContext

import datetime

def index(request):
    """docstring for index"""
    # request.LANGUAGE_CODE = 'el'
    return render_to_response('test.html',{'datenow':datetime.datetime.now()}, 
            context_instance=RequestContext(request))
    
