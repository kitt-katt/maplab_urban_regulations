from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # Подключаем маршруты нашего приложения tep_api
    path('api/v1/', include('tep_api.urls')),
]