from django import template
from dune.models import Category

register = template.Library()


@register.inclusion_tag('dune/list_categories.html')   # Вернет html
def show_categories(cat_selected=0):
    cats = Category.objects.all()
    return {'cats': cats, 'cat_selected': cat_selected}