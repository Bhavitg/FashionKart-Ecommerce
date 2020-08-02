"""ecom URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path,include,re_path
from products import views
from django.conf import settings
from django.conf.urls.static import static
from carts import views as cart_views
from orders import views as order_views
from accounts import views as acc_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('search/', views.search),
    path('contact_us/', views.contact_us, name="contact_us"),
    path('cart/', cart_views.view, name="cart"),
    path('checkout/', order_views.checkout, name="checkout"),
    path('checkout_final/', order_views.checkout_final, name="checkout_final"),
    path('orders/', order_views.orders, name="user_orders"),
    path('', views.home, name='home'),
    path('accounts/logout/', acc_views.logout_view, name='auth_logout'),
    path('accounts/login/', acc_views.login_view, name='auth_login'),
    path('accounts/register/', acc_views.registration_view, name='auth_register'),
    path('products/', views.all, name='products'),
    path('products/<str:slug>', views.single, name='single_product'),
    path('cart/<int:id>', cart_views.remove_from_cart, name='remove_from_cart'),
    #path('cart/<str:slug>/', cart_views.update_cart, name='update_cart'),
    re_path(r'^cart/(?P<slug>[\w-]+)/$', cart_views.add_to_cart, name='add_to_cart')
]


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)




#
# if settings.DEBUG:
#     urlpatterns+= static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
