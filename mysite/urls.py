from django.conf.urls import include, url
from django.contrib import admin
from rest_framework import routers
from blog import views

router = routers.DefaultRouter()
router.register(r'posts', views.PostViewSet)

urlpatterns = [
    url(r'^api/', include(router.urls)),
    url(r'^admin/', admin.site.urls),
    url(r'', include('blog.urls')),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]