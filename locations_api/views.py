from django.shortcuts import render
from rest_framework import viewsets, permissions

from locations.models import Country, City, Symbol
from locations_api.serializers import CitySerializer, CountrySerializer, SymbolSerializer


class CountryViewSet(viewsets.ModelViewSet):
    queryset = Country.objects.order_by('name')
    serializer_class = CountrySerializer
    permission_classes = [permissions.IsAuthenticated]


class CityViewSet(viewsets.ModelViewSet):
    queryset = City.objects.order_by('name')
    serializer_class = CitySerializer
    permission_classes = [permissions.IsAuthenticated]


class SymbolViewSet(viewsets.ModelViewSet):
    queryset = Symbol.objects.order_by('name')
    serializer_class = SymbolSerializer
    permission_classes = [permissions.IsAuthenticated]
