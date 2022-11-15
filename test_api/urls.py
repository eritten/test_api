from django.contrib import admin
from django.urls import path
from api.api_views import ProductView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
path('product/', ProductView.as_view(), name='product'),
    path('admin/', admin.site.urls),
]
if settings.DEBUG:
    urlpatterns+=static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
