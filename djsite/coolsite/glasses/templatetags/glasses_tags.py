from django import template
from glasses.models import *

register = template.Library()


@register.simple_tag()
def get_products():
    return Product.objects.all()


@register.inclusion_tag('glasses/product.html')
def show_product():
    prod = Product.objects.all()
    return {'prod': prod}
