from django.http import HttpResponse


def main(request):

    return HttpResponse("Main page")


def additional(request, _str='OK'):

    return HttpResponse(_str)
