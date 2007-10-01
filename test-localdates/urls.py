from django.conf.urls.defaults import *

urlpatterns = patterns('',
    # Example:
    
    # Uncomment this for admin:
     # (r'^admin/', include('django.contrib.admin.urls')),
     (r'.*', 'example.views.index')
     
     
)


