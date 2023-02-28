from django.contrib import admin

from .models import *


class GlassesAdmin(admin.ModelAdmin):
    list_display = ('id', 'Type', 'Title', 'Country', 'Company', 'Photo', 'Price')
    list_display_links = ('id', 'Title')
    search_fields = ('Title', 'Content')

admin.site.register(Product, GlassesAdmin)
