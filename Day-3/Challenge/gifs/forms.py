from django import forms
from .models import Category


class CategoryForm(forms.Form):
    name = forms.CharField(max_length = 30)


class GifForm(forms.Form):
    title = forms.CharField(max_length = 100)
    url = forms.URLField()
    uploader_name = forms.CharField(max_length = 50)
    category = forms.ModelMultipleChoiceField(queryset=Category.objects.all())