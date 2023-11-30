from django import template
from dune.models import Category, TagPost

register = template.Library()


@register.inclusion_tag('dune/list_categories.html')   # Вернет html
def show_categories(cat_selected=0):
    cats = Category.objects.all()
    return {'cats': cats, 'cat_selected': cat_selected}


@register.inclusion_tag('dune/list_tags.html')   # Вернет html
def show_all_tags():
    return {'tags': TagPost.objects.all()}