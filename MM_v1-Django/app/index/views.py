from random import randint
from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, 'index/index.html')


def random_number(request):
    return HttpResponse(randint(1, 99))
