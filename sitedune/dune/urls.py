from django.urls import path, register_converter
from . import views
from . import convertors

register_converter(convertors.FourDigitYearConverter, "year4")

urlpatterns = [
    path('', views.index, name='home'),   # http://127.0.0.1:8000/
    path('about/', views.about, name='about'),
    path('addpage/', views.addpage, name='add_page'),
    path('contact/', views.contact, name='contact'),
    path('login/', views.login, name='login'),
    path('post/<slug:post_slug>/', views.show_post, name='post'),
    path('categories/<slug:cat_slug>', views.show_category, name='category'),
    path('tag/<slug:tag_slug>', views.show_tag_postlist, name='tag')
]