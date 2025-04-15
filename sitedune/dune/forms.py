from django import forms
from .models import Category, Planet


class AddPostForm(forms.Form):
    title = forms.CharField(max_length=255, label='Заголовок', widget=forms.TextInput(attrs={'class': 'form-input'}))  # widget - стиль
    slug = forms.SlugField(max_length=255, label='URL')
    content = forms.CharField(widget=forms.Textarea(attrs={'cols': 50, 'rows': 5}), required=False, label='Контент')   # required=False - не обязательно
    is_published = forms.BooleanField(required=False, label='Статус', initial=True)
    cat = forms.ModelChoiceField(queryset=Category.objects.all(), label='Категория', empty_label='Категория не выбрана')
    planet = forms.ModelChoiceField(queryset=Planet.objects.all(), required=False, label='Планета', empty_label='Нет привязки к планете')
