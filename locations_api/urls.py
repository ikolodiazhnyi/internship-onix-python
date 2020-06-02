from django.urls import include, path
from rest_framework import routers
from locations_api.views import SymbolViewSet, CountryViewSet, CityViewSet

router = routers.DefaultRouter()
router.register(r'countries', CountryViewSet)
router.register(r'cities', CityViewSet)
router.register(r'symbols', SymbolViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls',
                              namespace='rest_framework')),
]