from django.urls import path
from locations import views


urlpatterns = [
    path('', views.main, name='main'),
    path('<str:line>/', views.additional)
]

