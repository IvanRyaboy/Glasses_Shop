from django.contrib.auth import logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.views import LoginView
from django.core.paginator import Paginator
from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy

from .forms import *
from .models import *
from .utils import DataMixin

menu = [{'title': 'О сайте', 'url_name': 'about'},
        {'title': 'Каталог', 'url_name': 'catalog'}]


def index(request):
    prod = Product.objects.all()
    return render(request, 'glasses/index.html', {'prod': prod, 'menu': menu, 'title': 'Главная страница'})


def catalog(request):
    prod = Product.objects.all()
    return render(request, 'glasses/catalog.html', {'prod': prod, 'menu': menu, 'title': 'Каталог'})


def about(request):
    contact_list = Product.objects.all()
    paginator = Paginator(contact_list, 3)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'glasses/about.html', {'page_obj': page_obj, 'menu': menu, 'title': 'О сайте'})


class LoginUser(DataMixin, LoginView):
    form_class = AuthenticationForm
    template_name = 'glasses/login.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Авторизация")
        return dict(list(context.items()) + list(c_def.items()))

    def get_success_url(self):
        return reverse_lazy('home')


def logout_user(request):
    logout(request)
    return redirect('login')


def show_item(request, item_id):
    if request.method == 'POST':
        form = OrderCreate(request.POST)
        if form.is_valid():
            order = form.save()
            print(order)
    else:
        form = OrderCreate

    prod = get_object_or_404(Product, pk=item_id)

    context = {
        'form': form,
        'prod': prod,
        'menu': menu,
        'title': prod.Title,
    }

    return render(request, 'glasses/product.html', context=context)


def register(request):
    form = RegisterUserForm()
    if request.method == 'POST':
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        else:
            form = RegisterUserForm()
    success_url = reverse_lazy('login')
    context = {
        'form': form,
        'menu': menu,
        'title': 'Регистрация'
    }

    return render(request, 'glasses/register.html', {'form': form, 'menu': menu, 'title': 'Регистрация'})


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