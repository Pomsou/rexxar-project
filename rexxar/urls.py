from django.contrib import admin
from django.urls import path
import news.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', news.views.home, name='home'),
]
