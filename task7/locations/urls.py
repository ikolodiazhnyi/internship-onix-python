from django.urls import path
from locations import views


urlpatterns = [
    path('', views.main, name='main'),
    path('additional', views.additional)
]

