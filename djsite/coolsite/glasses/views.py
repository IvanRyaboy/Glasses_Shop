from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, get_object_or_404

from .forms import *
from .models import *

menu = [{'title': 'О сайте', 'url_name': 'about'},
        {'title': 'Каталог', 'url_name': 'catalog'},
        {'title': 'Регистрация', 'url_name': 'authorization'}]


def index(request):
    prod = Product.objects.all()
    return render(request, 'glasses/index.html', {'prod': prod, 'menu': menu, 'title': 'Главная страница'})


def catalog(request):
    prod = Product.objects.all()
    return render(request, 'glasses/catalog.html', {'prod': prod, 'menu': menu, 'title': 'Каталог'})


def about(request):
    return HttpResponse("О сайте")


def authorization(request):
    if request.method == 'POST':
        form = AddUser(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
    else:
        form = AddUser()
    return render(request, 'glasses/authorization.html', {'form': form, 'menu': menu, 'title': 'Авторизация'})




def show_item(request, item_id):
    prod = get_object_or_404(Product, pk=item_id)

    context = {
        'prod': prod,
        'menu': menu,
        'title': prod.Title,
    }

    return render(request, 'glasses/product.html', context=context)


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