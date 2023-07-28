from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound, Http404
from .models import *
# Create your views here.
menu = ["О сайте", "Добавить статью", "Обратная связь", "Войти"]

def page(request):
    return render(request,"base/page.html")
def index(request):
    posts = Product.objects.all()
    return render(request, 'base/index.html', {'posts': posts, 'menu': menu, 'title': 'Главная страница'})

def about(request):
    return render(request, 'base/about.html', {'menu': menu, 'title': 'О сайте'})
def mainpage(request):
    return render(request,"base/base.html",{"menu":menu, 'title': 'Главная страница'})
def categories(request,birthid):
    objects=Product.objects.all()
    return render(request,"base/category.html",{"objects":objects})
def archive(request, year):
    # перенаправления сайта
    # if (int(year) > 2020):
    #     return redirect('category')
    return render(request,"base/archive.html")
def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')
