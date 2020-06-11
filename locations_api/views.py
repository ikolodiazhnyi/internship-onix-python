from django.shortcuts import render, get_object_or_404
from rest_framework import viewsets, permissions, generics

from locations.models import Country, City, Symbol
from locations_api.serializers import CitySerializer, CountrySerializer, SymbolSerializer, CountryIdSerializer


class CountryViewSet(viewsets.ModelViewSet):
    queryset = Country.objects.order_by('name')
    serializer_class = CountrySerializer
    permission_classes = [permissions.IsAuthenticated]


class CityViewSet(viewsets.ModelViewSet):
    queryset = City.objects.order_by('name')
    serializer_class = CitySerializer

    def get_queryset(self):
        serializer = CountryIdSerializer(data=self.request.query_params)
        serializer.is_valid(raise_exception=True)
        country_id = serializer.validated_data['country_id']
        country = get_object_or_404(Country, id=country_id)
        self.queryset = City.objects.filter(country=country)

        return self.queryset


class SymbolViewSet(viewsets.ModelViewSet):
    queryset = Symbol.objects.order_by('name')
    serializer_class = SymbolSerializer
    permission_classes = [permissions.IsAuthenticated]


class CountryListCreate(generics.ListCreateAPIView):
    queryset = Country.objects.order_by('name')
    serializer_class = CountrySerializer


class CountryRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Country.objects.order_by('name')
    serializer_class = CountrySerializer
