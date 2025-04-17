from django import forms
from django.core.exceptions import ValidationError
from django.utils.deconstruct import deconstructible
from .models import Category, Planet, Dune
from django.core.validators import MinLengthValidator, MaxLengthValidator
import PIL


# Для многократного использования на разных формах
@deconstructible
class RussianValidator:
    ALLOWED_CHARS = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЬЫЪЭЮЯабвгдеёжзийклмнопрстуфхцчшщьыъэюя0123456789- '
    code = 'russian'

    def __init__(self, message=None):
        self.message = message if message else 'Должны присутствовать только русские символы, дефис и пробел'

    def __call__(self, value, *args, **kwargs):
        if not (set(value) <= set(self.ALLOWED_CHARS)):
            raise ValidationError(self.message, code=self.code)


class AddPostForm(forms.ModelForm):
    cat = forms.ModelChoiceField(queryset=Category.objects.all(), label='Категория', empty_label='Категория не выбрана')
    planet = forms.ModelChoiceField(queryset=Planet.objects.all(), required=False,
                                    label='Планета', empty_label='Нет привязки к планете')

    class Meta:
        model = Dune
        fields = ['title', 'slug', 'content', 'is_published', 'cat', 'tags', 'planet']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-input'}),
            'content': forms.Textarea(attrs={'cols': 50, 'rows': 5})
        }
        labels = {'slug': 'URL'}

    def clean_title(self):
        title = self.cleaned_data['title']
        if len(title) > 50:
            raise ValidationError("Длина заголовка превышает 50 символов")


class UploadFileForm(forms.Form):
    file = forms.ImageField(label='Файл')