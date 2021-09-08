from django.contrib import admin
from django.urls import path, include
from qrtoolkit_core import urls as qr_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(qr_urls.api_routes)),
    path('', include(qr_urls.code_routes))
]
