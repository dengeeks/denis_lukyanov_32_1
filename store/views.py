from django.shortcuts import render
from django.shortcuts import HttpResponse
# Create your views here.
from datetime import datetime


def hello_func(request):
    return HttpResponse('Hello! Its my project')


def date_func(request):
    return HttpResponse(f'Сегодняшняя дата - {datetime.now()}')

def good_by_user_func(request):
    return HttpResponse('Goodby User!')