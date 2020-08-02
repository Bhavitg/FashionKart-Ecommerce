from django.db import models

# Create your models here.
from carts.models import Cart
from django.contrib.auth import get_user_model

User = get_user_model()

STATUS_CHOICES=(
    ("Started","Started"),
    ("Abandoned","Abandoned"),
    ("Finished","Finished"),
)

class Order(models.Model):
    sub_total = models.DecimalField(default=0.00, max_digits=1000, decimal_places=2)
    tax_total = models.DecimalField(default=0.00, max_digits=1000, decimal_places=2)
    final_total = models.DecimalField(default=0.00, max_digits=1000, decimal_places=2)
    cart = models.ForeignKey(Cart,on_delete=models.CASCADE)
    order_id = models.CharField(max_length=120 ,unique=True, default='ABC')
    status = models.CharField(max_length = 120 , choices= STATUS_CHOICES , default="started")
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    update = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __unicode__(self):
        return self.order_id