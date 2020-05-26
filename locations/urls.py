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
    path('add/country/', views.add_country, name='add_new_country'),
    path('add/city/<int:id_country>/', views.add_city, name='add_new_city'),
    path('edit/country/<int:id_country>/', views.edit_country, name='edit_country'),
    path('edit/city/<int:id_city>/', views.edit_city, name='edit_city'),
    path('<str:line>/', views.additional)
]
