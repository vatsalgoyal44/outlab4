from django.urls import path,re_path
from django.conf.urls import url
from . import views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    url(r'^$', views.explore),
    url(r'^login/$', 
        LoginView.as_view(template_name='accounts/login.html'), 
        name="login"),
    url(r'^logout/$', 
        LogoutView.as_view(template_name='accounts/login.html'), 
        name="logout"),
    url(r'^signup/$',views.signup,name = "signup"),
    url(r'^profile/$',views.profile,name = "profile"),
    url(r'^profile/(?P<pk>\d+)/$',views.profile,name = "profile_pk"),
    url(r'^explore/$',views.explore,name = "explore"),
    url(r'^update/(?P<pk>\d+)/$',views.update,name = "update"),
]