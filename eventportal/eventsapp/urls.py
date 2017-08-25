from django.conf.urls import url
from . import views

urlpatterns = [

    url(r'^$', views.home, name='home'),
    url(r'^(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/'
        r'(?P<event>[-\w]+)/$', views.event_detail, name='event_detail'),
    url(r'^register/$', views.user_register, name='register'),
    url(r'^login/$', views.user_login, name='login'),
    url(r'^logout/$', views.user_logout, name='logout'),
    url(r'^attend/(?P<event_id>\d+)/$', views.attend_event, name='attend'),
]
