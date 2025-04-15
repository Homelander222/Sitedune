from django import forms
from django.core.exceptions import ValidationError
from django.utils.deconstruct import deconstructible

from .models import Category, Planet
from django.core.validators import MinLengthValidator, MaxLengthValidator


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


class AddPostForm(forms.Form):
    title = forms.CharField(min_length=5, max_length=255, label='Заголовок',
                            widget=forms.TextInput(attrs={'class': 'form-input'}),
                            validators=[
                                RussianValidator()
                            ],
                            error_messages={
                                'min_length': 'Слишком короткий заголовок',
                                'required': 'Необходим заголовок'

                            })  # widget - стиль
    slug = forms.SlugField(max_length=255, label='URL',
                           validators=[
                               MinLengthValidator(5, message="Минимум 5 символов"),
                               MaxLengthValidator(100, message="Максимум 100 символов")
                           ])
    content = forms.CharField(widget=forms.Textarea(attrs={'cols': 50, 'rows': 5}), required=False, label='Контент')   # required=False - не обязательно
    is_published = forms.BooleanField(required=False, label='Статус', initial=True)
    cat = forms.ModelChoiceField(queryset=Category.objects.all(), label='Категория', empty_label='Категория не выбрана')
    planet = forms.ModelChoiceField(queryset=Planet.objects.all(), required=False, label='Планета', empty_label='Нет привязки к планете')

    #   Для использования в одном поле в текущей форме
    # def clean_title(self):
    #     title = self.cleaned_data['title']
    #     ALLOWED_CHARS = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЬЫЪЭЮЯабвгдеёжзийклмнопрстуфхцчшщьыъэюя0123456789- '
    #     if not (set(title) <= set(ALLOWED_CHARS)):
    #         raise ValidationError('Должны присутствовать только русские символы, дефис и пробел')

