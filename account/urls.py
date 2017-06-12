from django.conf.urls import url
from . import views
from django.conf import settings
from django.views.static import serve


app_name = 'account'
urlpatterns = [
    url(r'^account/$', views.IndexView.as_view(), name='index'),
    url(r'^account/(?P<pk>\d+)/$', views.DetailView.as_view(), name="detail"),
    url(r'^account/(?P<operation>.+)/(?P<pk>\d+)/$',
        views.change_to_favorite, name="changefavorite"),
    url(r'^account/mybooks/$', views.ListMybooks.as_view(), name='mybooks')
]


if settings.DEBUG:
    urlpatterns += [
        url(r'^media/(?P<path>.*)$', serve, {
            'document_root': settings.MEDIA_ROOT,
        }),
        ]
