from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView
from django.views.generic import RedirectView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('careers.urls')),
    path('swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
    path('api/internal-schema/', SpectacularAPIView.as_view(), name='schema'),
    path('', RedirectView.as_view(url='swagger-ui/', permanent=False)),
]
