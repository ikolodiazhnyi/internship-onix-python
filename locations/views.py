from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect

from locations.models import Country, City


@login_required
def main(request):
    return HttpResponse("Main page")


@login_required
def additional(request, line):
    return HttpResponse(line)


@login_required
def get_countries(request, *args, **kwargs):
    countries_objs = Country.objects.order_by('name')

    content = {
        'countries': countries_objs,
    }

    return render(request, 'locations/countries.html', content)


@login_required
def get_country_and_cities(request, id_country):
    if request.user.is_authenticated:
        country_name = get_object_or_404(Country, id=id_country)
        cities_of_country = country_name.city_set.all()

        content = {
            'cities': cities_of_country,
            'country': country_name,
        }

        return render(request, 'locations/country.html', content)
    else:
        return redirect('/login/')


@login_required
def get_city(request, id_city):
    city_obj = get_object_or_404(City, id=id_city)

    content = {
        'city': city_obj,
    }

    return render(request, 'locations/city.html', content)


def delete_city(request, id_city):
    city = get_object_or_404(City, id=id_city)
    city.delete()

    return redirect('country', city.country.id)
