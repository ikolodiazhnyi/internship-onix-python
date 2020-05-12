from django.urls import path
from locations import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.main, name='main'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('countries/', views.get_countries, name='countries'),
    path('country/<int:id_country>/', views.get_country_and_cities, name='country'),
    path('city/<int:id_city>/', views.get_city, name='cities'),
    path('delete/<int:id_city>/', views.delete_city, name='delete_cities'),
    path('<str:line>/', views.additional)
]
