from django.urls import include, path
from rest_framework import routers
from locations_api.views import CityViewSet, CountryRetrieveUpdateDestroy, \
    CountryListCreate

router = routers.SimpleRouter()
router.register(r'cities', CityViewSet)

urlpatterns = [
    path('countries/', CountryListCreate.as_view()),
    path('countries/<int:pk>/', CountryRetrieveUpdateDestroy.as_view()),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]