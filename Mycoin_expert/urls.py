
from django.contrib import admin
from django.urls import path,include, re_path
from django.views.static import serve
from django.conf import settings

urlpatterns = [
    re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
    re_path(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT}),
    path('admin/', admin.site.urls),
    path('', include('mycoinApp.urls')),
    path('c-', include(('chat.urls', "chat"), namespace="chat")),
]
