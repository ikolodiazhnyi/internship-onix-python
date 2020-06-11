from rest_framework import serializers, viewsets

from locations.models import Country, City, Symbol


class CountrySerializer(serializers.ModelSerializer):
    name = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Country
        fields = [
            'name',
            'description',
            'population',
            'flag',
            'cities_count',
        ]


class CountryIdSerializer(serializers.Serializer):
    country_id = serializers.IntegerField()


class CitySerializer(serializers.ModelSerializer):
    country = CountrySerializer()

    class Meta:
        model = City
        fields = [
            'name',
            'country',
            'longitude',
            'latitude',
        ]


class SymbolSerializer(serializers.ModelSerializer):
    image = serializers.ImageField()

    class Meta:
        model = Symbol
        fields = [
            'image',
        ]
