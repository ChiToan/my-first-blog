from django.conf.urls import url
from . import views
from django.contrib.auth import views as auth_views
from blog import views as core_views

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
    url(r'^$', views.post_list, name='home'),
    url(r'^post/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
	url(r'^post/(?P<pk>\d+)/edit/$', views.post_edit, name='post_edit'),
    url(r'^post/new/$', views.post_new, name='post_new'),
    url(r'^signup/$', core_views.signup, name='signup'),
    url(r'^login/$', auth_views.login, {'template_name': 'login.html'}, name='login'),
    url(r'^logout/$', auth_views.logout, name='logout'),
]
