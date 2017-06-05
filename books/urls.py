from django.conf.urls import url
from . import views
from django.contrib.auth.views import login

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^register/$', views.UserFormView.as_view(), name='register'),
    url(r'^logout/$', views.Logout, name='logout'),
    url(r'^login/$', login, {'template_name': 'home/login.html'}, name='login'),
]
