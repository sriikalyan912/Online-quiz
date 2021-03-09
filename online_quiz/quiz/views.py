from django.http import HttpResponse


def index(request):
    res = "<h1>Hello World!"
    return HttpResponse(res)