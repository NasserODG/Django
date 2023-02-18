from django import forms
from gifs.models import Category, Gif


class GifForm(forms.ModelForm):
     class Meta:
        models = Gif
        fields = ('title', 'url', 'uploader_name', 'categories = forms.ModelMultipleChoiceField(queryset=None)')
        

class CategoryForm(forms.ModelForm):
    class Meta:
        models = Category
        fields = ('name = models.CharField(max_length=100, null=True)',)
        
