from django.conf.urls.defaults import *
from mysite.views import hello, current_datetime, hours_ahead
from mysite.books import views
from mysite.contact.views import contact, contact_thanks

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    ('^hello/$', hello),        
    ('^time/$', current_datetime),
    (r'^time/plus/(\d{1,2})$', hours_ahead),
    (r'^admin/', include(admin.site.urls)),
    (r'^search/$', views.search),
    (r'^contact/$', contact),
    (r'^contact/thanks/$', contact_thanks),
)
