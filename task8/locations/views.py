from django.http import HttpResponse


def main(request):

    return HttpResponse("Main page")


def additional(request, line):

    return HttpResponse(line)
