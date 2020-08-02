import string
import random
from .models import Order
def id_gen(size=6, chars = string.ascii_uppercase + string.digits):
    the_id = "".join(random.choice(chars) for x in range(size))
    try:
        order = Order.objects.get(order_id=the_id)
        id_gen()
    except Order.DoesNotExist:
        return the_id
    return the_id


print(id_gen())