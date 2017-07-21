from . import views
from django.conf.urls import url
app_name='todo'
urlpatterns = [
    url(r'newlist/$',views.listnew.as_view(),name='listnew'),
    url(r'newitem/(?P<pk>[0-9]+)/$',views.itemnew.as_view(),name='itemnew'),
    url(r'lists/$',views.listtodo.as_view(),name='lists'),
    url(r'list/(?P<pk>[0-9]+)/$',views.itemtodo.as_view(),name='items'),
    url(r'listup/(?P<pk>[0-9]+)/$', views.listupdate.as_view(), name='listup'),
    url(r'itemup/(?P<pk>[0-9]+)/$', views.itemupdate.as_view(), name='itemup'),
    url(r'itemupd/(?P<pk>[0-9]+)/$', views.itemupd.as_view(), name='itemupd'),
]