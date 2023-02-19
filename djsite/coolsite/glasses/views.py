from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render

def index(request):
    return HttpResponse("Магазин очков")


def cats(request, catid):
    if request.POST:
        print(request.POST)
    return HttpResponse(f"<h1> Статья категории </h1><p>{catid}</p>")


def archive(request, year):
    if int(year) > 2023:
        return Http404()
    return HttpResponse(f"<h1>Архив по годам</h1><p>{year}</p>")


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')