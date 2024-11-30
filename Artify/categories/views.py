from django.shortcuts import render
from .models import ArtCategory

def category_list(request):
    categories = ArtCategory.objects.all()
    return render(request, 'categories/category_list.html', {'categories': categories})


def homepage(request):
    return render(request, 'categories/homepage.html')


def about_page(request):
    return render(request, 'categories/about.html')
