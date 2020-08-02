from django.shortcuts import render , Http404
from products.models import Product, ProductImage

# Create your views here.
def home(request):

    products = Product.objects.all()
    template = "home.html"
    context = {"products": products}
    return render(request, template, context)

def all(request):
    products = Product.objects.all()
    context = {'products': products}
    template = 'all.html'
    return render(request, template, context)


def search(request):
    try:
        q = request.GET.get('q')
    except:
        q = None
    if q:
        products = Product.objects.filter(title__icontains=q)
        context = {'query':q, 'products':products}
        template = 'results.html'
    else:
        context = {}
        template = 'home.html'

    return render(request, template, context)

def single(request,slug):

        product = Product.objects.get(slug=slug)
        #images = Product.productimage_set.all()
        images = ProductImage.objects.filter(product=product)
        context = {'product': product, 'images': images}
        template = 'single.html'
        return render(request, template, context)


def contact_us(request):
    context={}
    template='contact_us.html'
    return render(request,template,context)