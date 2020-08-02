import stripe
from django.db import models
from django.conf import settings
from django.contrib.auth.signals import user_logged_in
# Create your models here.

class UserStripe(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    stripe_id = models.CharField(max_length = 120)

    def __unicode__(self):
        return str(self.stripe_id)

