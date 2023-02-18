from django.shortcuts import render, redirect
from .models import Gif, Category
from .forms import GifForm, CategoryForm

# Create your views here.
def gif(request):
    gif_all = Gif.objects.all()
    return render(request, 'gif/Homepage_view.html', { "git_all": gif_all})

def gif_method(request, id):
    gif_meth = Gif.objects.get(id=id)
    return render(request, 'gif/gif_view.html', {"gif_meth": gif_meth})

def category(request):
    categorie = Category.objects.all()
    return render (request, 'git/category_view.html', {"categorie": categorie})

def category_method(request, id):
    cat_meth = Category.objects.get(id=id)
    return render (request, 'gif/category_list_view.html', {"cat_meth": cat_meth})

def AddCategory(request, name):
    categorie = Category.objects.get(name=name)
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            form = CategoryForm()
    else :
        form = CategoryForm()
    context = {
            "category": category,
            "form": form
    }
    return (render, 'gif/AddCategory_view.html', context)

def AddGif(request, name):
    gif = Gif.objects.get(name=name)
    if request.method == 'POST':
        form = GifForm(request.POST)
        if form.is_valid():
            form.save()
            form = GifForm()
    else :
        form = GifForm()
    context = {
            "gif": gif,
            "form": form
    }
    return (render, 'gif/AddGif_view.html', context)
         