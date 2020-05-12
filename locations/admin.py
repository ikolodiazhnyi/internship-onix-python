from django.contrib import admin
from .models import Symbol, Country, City
# Register your models here.


class CountryAdmin(admin.ModelAdmin):
    search_fields = ['name']


class CityAdmin(admin.ModelAdmin):
    list_filter = ['country']


admin.site.register(Symbol)
admin.site.register(Country, CountryAdmin)
admin.site.register(City, CityAdmin)
