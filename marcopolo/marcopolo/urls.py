from django.conf.urls import patterns, include, url
from django.contrib import admin
from rest_framework import routers
from game import views

router = routers.DefaultRouter()
router.register(r'usuarios', views.UsuarioViewSet, 'usuarios')

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'marcopolo.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^admin/', include(admin.site.urls)),
)
