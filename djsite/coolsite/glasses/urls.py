from django.urls import path, re_path

from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('about/', about, name='about'),
    path('catalog/', catalog, name='catalog'),
    path('login/', LoginUser.as_view() , name='login'),
    path('logout/', logout_user, name='logout'),
    path('register/', register, name='register'),
    path('item/<int:item_id>/', show_item, name='item')
]

