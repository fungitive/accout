from django.conf.urls import url
from . import views
app_name='myaccounts'
urlpatterns = [
    url(r'^profile/$', views.profile, name='profile'),
    url(r'^profile/update/$', views.profile_update, name='profile_update'),
]