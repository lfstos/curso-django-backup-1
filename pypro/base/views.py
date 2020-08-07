# Create your views here.
from django.http import HttpResponse


def hello(request):
    return HttpResponse('Sistema em construção!')
