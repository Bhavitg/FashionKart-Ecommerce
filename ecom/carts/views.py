from django.shortcuts import render ,HttpResponseRedirect, Http404
from django.urls import reverse
from decimal import Decimal

# Create your views here.
from .models import Cart, CartItem
from products.models import Product
from django.contrib import sessions



def view(request):
    try:
        the_id = request.session["cart_id"]
        cart = Cart.objects.get(id=the_id)
    except:
        the_id =None
    if the_id:
        context = {"cart": cart}
    else:
        context = {"empty": True}
    template = "cart/view.html"
    return render(request, template, context)

def remove_from_cart(request,id):
    try:
        the_id = request.session["cart_id"]
        cart = Cart.objects.get(id=the_id)
    except:
        return HttpResponseRedirect(reverse("cart"))
    cartitem = CartItem.objects.get(id=id)
    cartitem.cart=None
    cartitem.save()

    new_total = 0.00
    for item in cart.cartitem_set.all():
        line_total = float(item.product.price) * item.quantity
        new_total += line_total
    request.session['items_total'] = cart.cartitem_set.count()
    cart.total = Decimal(new_total)
    cart.save()
    # cartitem.delete()
    #send success message
    return HttpResponseRedirect(reverse("cart"))


def add_to_cart(request, slug):
    try:
        qty=request.GET.get('qty')
        update_qty = True
    except:
        qty=None
        update_qty = False
    try:
        the_id = request.session["cart_id"]
    except:
        new_cart = Cart()
        new_cart.save()
        request.session["cart_id"]=new_cart.id
        the_id = new_cart.id
    cart = Cart.objects.get(id=the_id)
    try:
        product = Product.objects.get(slug=slug)
    except Product.DoesNotExist:
        pass
    except:
        pass
    cart_item , created = CartItem.objects.get_or_create(cart=cart,product=product)
    if created:
        print("dfgfd")
    if qty and update_qty:
        cart_item.quantity=qty
        cart_item.save()
    else:
        pass
    # if not cart_item in cart.items.all():
    #     cart.items.add(cart_item)
    # else:
    #     cart.items.remove(cart_item)
    new_total=0.00
    for item in cart.cartitem_set.all():
        line_total = float(item.product.price)*item.quantity
        new_total += line_total
    request.session['items_total']=cart.cartitem_set.count()
    cart.total = Decimal(new_total)
    cart.save()
    return HttpResponseRedirect(reverse("cart"))

