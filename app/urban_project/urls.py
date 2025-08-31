from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView, SpectacularRedocView


urlpatterns = [
    path('admin/', admin.site.urls),
    # Подключаем маршруты нашего приложения tep_api
    path('api/v1/', include('tep_api.urls')),
    # Маршруты для документации OpenAPI
    path('api/v1/schema/', SpectacularAPIView.as_view(), name='schema'),
    # Swagger UI:
    path('api/v1/schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    # Redoc:
    path('api/v1/schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
]