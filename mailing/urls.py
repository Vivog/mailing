from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from mailing import settings

urlpatterns = [
    path('', admin.site.urls),
    path('ckeditor/', include('ckeditor_uploader.urls')),

]

if settings.DEBUG:
    import debug_toolbar.urls
    urlpatterns = [
                      path('__debug__/', include('debug_toolbar.urls')),
                  ] + urlpatterns
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
