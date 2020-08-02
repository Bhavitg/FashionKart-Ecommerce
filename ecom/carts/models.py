
from django.db import models
from products.models import Product

# Create your models here.4
class CartItem(models.Model):
    cart = models.ForeignKey('Cart',on_delete=models.CASCADE, null=True, blank=True)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    update = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __unicode__(self):
        try:
            return str(self.cart.id)
        except:
            return self.product.title
class Cart(models.Model):
    #items = models.ManyToManyField(CartItem,blank=True)
    #products = models.ManyToManyField(Product,blank=True)
    total = models.DecimalField(decimal_places=2, max_digits=100, default=29.9)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    update = models.DateTimeField(auto_now_add=False, auto_now=True)
    active = models.BooleanField(default=True)

def ___unicode__(self):
    return self.id