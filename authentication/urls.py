from django.conf.urls import *
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token, verify_jwt_token
from . import views

app_name='authentication'
urlpatterns = [
    url(r'^auth-token/', obtain_jwt_token),
    url(r'^login/',views.akarsh),
    url(r'^restricted/$', views.RestrictedView.as_view()),
    url(r'^token-refresh/', refresh_jwt_token),
    url(r'^token-verify/', verify_jwt_token),
    url(r'^register/$', views.AuthRegister.as_view()),
    url(r'^logout/$',views.logout.as_view(),name='logout'),
    url(r'^profile/(?P<pk>[0-9]+)/$', views.updateprofile.as_view()),
]