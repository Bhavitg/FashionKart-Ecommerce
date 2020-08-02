import stripe
from django.db import models
from django.conf import settings
from django.contrib.auth.signals import user_logged_in
from .models import UserStripe
# Create your models here.
stripe.api_key = settings.STRIPE_SECRET_KEY

def get_or_create_stripe(sender,user,*args,**kwargs):
    # Create a Customer:
    try:
        user.usersstripe.stripe_id
    except UseStripe.DoesNotExists :
        customer = stripe.Customer.create(
        email=str(user.email),
        )
        new_user_stripe = UseStripe.objects.create(
            user=user,
            stripe_id = customer.id
        )
    except:
        pass


user_logged_in.connect(get_or_create_stripe)