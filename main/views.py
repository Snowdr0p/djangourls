from django.shortcuts import render
from django.http import HttpResponse


def make_header(s):
    return f'<h1 align="center">{s}</h1>'


def print_name(request):
    return HttpResponse(make_header('Dean'))


def print_surname(request):
    return HttpResponse(make_header('Winchester'))


def print_age(request):
    return HttpResponse(make_header('25 y.o.'))


def print_name_surname(request):
    return HttpResponse(make_header('Dean Winchester'))


def print_name_surname_age(request):
    return HttpResponse(make_header('Dean Winchester, 25 y.o.'))
