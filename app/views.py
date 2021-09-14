from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.template import loader
from .models import Product


def index(request):
    product = Product.objects.all()
        
    context = {
        'course': 'Django Framework Course Recap',
        'another_key': 'Another Value From another_key \
            inside a context object',
        'product': product
    }
    return render(request, 'index.html', context)


def contact(request):
    return render(request, 'contact.html')


def product(request, id):
    #product_id = Product.objects.get(id=id)
    product_id = get_object_or_404(Product, id=id)
    context = {
        'product': product_id
    }
    return render(request, 'product.html', context)


def error404(request, ex):
    """ Development Only (see on settings.py) """
    template = loader.get_template('404.html')
    return HttpResponse(content=template.render(), content_type='text/html; charset=utf8', status=404)

def error500(request):
    """ Production Only (see on settings.py) """
    template = loader.get_template('500.html')
    return HttpResponse(content=template.render(), content_type='text/html; charset=utf8', status=500)
