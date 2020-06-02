from locations.models import Country


def show_country_list(get_response):

    def middleware(request):
        request.country_list = Country.objects.order_by('name')
        response = get_response(request)

        return response

    return middleware
