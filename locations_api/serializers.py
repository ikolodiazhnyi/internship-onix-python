from rest_framework import serializers

from locations.models import Country, City, Symbol


class CountrySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Country
        fields = [
            'name',
            'description',
            'population',
            'flag',
            'cities_count',
        ]


class CitySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = City
        fields = [
            'name',
            'country',
            'longitude',
            'latitude',
        ]


class SymbolSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Symbol
        fields = [
            'image',
        ]
