from django import forms
from .models import Category, Planet


class AddPostForm(forms.Form):
    title = forms.CharField(max_length=255)
    slug = forms.SlugField(max_length=255)
    content = forms.CharField(widget=forms.Textarea(), required=False)   # required=False - не обязательно
    is_published = forms.BooleanField(required=False)
    cat = forms.ModelChoiceField(queryset=Category.objects.all())
    planet = forms.ModelChoiceField(queryset=Planet.objects.all(), required=False)
