from django.contrib import admin
from django.urls import include, path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.main),
    path('home/', views.home),
    path('about/', views.about)
]
