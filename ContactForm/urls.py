from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    # Подключаем маршруты вашего приложения напрямую без префиксов
    # (Замените 'contact_app', если папка приложения называется иначе)
    path('', include('contact_app.urls')),
]
