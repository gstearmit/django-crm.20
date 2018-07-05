from django.conf.urls import url, include
from django.contrib.auth import views
from django.conf import settings
app_name = 'crm'


urlpatterns = [

    url(r'^', include('common.urls', namespace='common')),
    url(r'^accounts/', include('accounts.urls', namespace='accounts')),
    url(r'^leads/', include('leads.urls', namespace='leads')),
    url(r'^contacts/', include('contacts.urls', namespace='contacts')),
    url(r'^opportunities/', include('opportunity.urls', namespace='opportunities')),
    url(r'^cases/', include('cases.urls', namespace='cases')),
    url(r'^emails/', include('emails.urls', namespace='emails')),
    #url(r'^planner/', include('planner.urls', namespace='planner')),
    url(r'^logout/$', views.logout, {'next_page': '/login/'}, name='logout'),
]

if settings.DEBUG:
       import debug_toolbar
       urlpatterns += [
           url(r'^__debug__/', include(debug_toolbar.urls)),
       ]