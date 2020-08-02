from django.shortcuts import render , HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
import time
from products.models import Product
from carts.models import Cart,CartItem
# Create your views here.
from .models import Order
from .utils import id_gen

def orders(request):
    context={    }
    template = "orders/user.html"
    return render(request,template,context)

#Login Required
@login_required
def checkout(request):

    try:
        the_id = request.session["cart_id"]
        cart = Cart.objects.get(id=the_id)
    except:
        the_id = None
        return HttpResponseRedirect(reverse("cart"))

    try:
        new_order = Order.objects.get(cart = cart)
    except Order.DoesNotExist:
        new_order = Order()
        new_order.user = request.user
        new_order.order_id = id_gen()#str(time.time())
        new_order.cart_id = the_id
        new_order.save()
        del request.session['cart_id']
        del request.session['items_total']
        return HttpResponseRedirect(reverse("home"))       #order successfulllllllll
    except:
        return  HttpResponseRedirect(reverse("cart"))

    if new_order.status=="Finished":
        del request.session['cart_id']
        del request.session['items_total']
        return HttpResponseRedirect(reverse("cart"))


    context={}
    template= "home.html"
    return render(request,template,context)


def checkout_final(request):
    try:
        the_id = request.session["cart_id"]
        cart = Cart.objects.get(id=the_id)
    except:
        the_id =None
    if the_id:
        context = {"cart": cart}
    else:
        context = {"empty": True}
    template="checkout_final.html"
    return render(request, template, context)
