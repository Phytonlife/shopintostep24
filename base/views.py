from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound, Http404

# Create your views here.
def mainpage(request):
    return render(request,"base/category.html")
def categories(request,birthid):
    if request.GET:
        print(request.GET)
    return render(request,"base/category.html")
def archive(request, year):
    # перенаправления сайта
    # if (int(year) > 2020):
    #     return redirect('category')
    return render(request,"base/archive.html")
def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')
