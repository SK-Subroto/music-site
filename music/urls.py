from django.urls import path
from django.conf.urls import url
from . import views
app_name = 'music'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),

    # /music/id
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),

    # /music/album/add/
    url(r'album/add/$', views.AlbumCreate.as_view(), name='album-add'),
]