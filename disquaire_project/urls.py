from django.conf import settings
from django.conf.urls import include, url
from django.contrib import admin
from store import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^store/', include(('store.urls','store'), namespace='store')),
    #url(r'^store/', include('store.urls')),
    url(r'^admin/', admin.site.urls)
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns