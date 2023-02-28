from django.urls import path, re_path

from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('about/', about, name='about'),
    path('catalog/', catalog, name='catalog'),
    path('authorization/', authorization, name='authorization'),
    path('item/<int:item_id>/', show_item, name='item')
]

