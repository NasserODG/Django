from django.shortcuts import render, HttpResponse, redirect
from .models import Gif, Category
from .forms import CategoryForm, GifForm

# Create your views here.
def homepage(request):
	context = { 'gifs': Gif.objects.all(), 'categories': Category.objects.all() }
	return render(request, 'homepage.html', context)

def category(request, category_id):
	return render(request, 'category.html', { 'category': Category.objects.get(id = category_id) })

def gif(request, gif_id):
	return render(request, 'gif.html', { 'gif': Gif.objects.get(id = gif_id) })

def add_category(request):
	if request.method == 'GET':
		form = CategoryForm()
		return render(request, 'add.html', { 'form':form, 'add_type':'Category' })

	if request.method == 'POST':
		form = CategoryForm(request.POST)
		if form.is_valid():
			cat = Category.objects.create(name=form.cleaned_data['name'])
		return redirect('category', cat.id)

def add_gif(request):
	if request.method == 'GET':
		form = GifForm()
		return render(request, 'add.html', { 'form':form, 'add_type':'Gif' })

	if request.method == 'POST':
		form = GifForm(request.POST)
		if form.is_valid():
			gif = Gif.objects.create(title = form.cleaned_data['title'], url = form.cleaned_data['url'], uploader_name = form.cleaned_data['uploader_name'])
			gif.category.set(form.cleaned_data['category'])
		return redirect('gif', gif.id)