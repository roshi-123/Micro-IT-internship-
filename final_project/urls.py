"""final_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path
from final_project import views as fv
from cobalt_app import views as av
from cart_app import views as cv
from django.conf import settings
from django.conf.urls.static import static
from paymentapp import views as pav
from wishlistapp import views as wv
urlpatterns = [
    path('admin/', admin.site.urls),
    path("",fv.indexs,name="index"),
   path("register",av.registers,name="register"),
    path("login",av.logins,name="login"),
    path('logout/',av.logout_view, name='logout'),  # Add logout URL
    path('productview/<int:pk>',av.product_view,name='product_view'),
    path('categoryview/<str:pic>',av.category_view,name='category_view'),
    path('all-products/', av.all_products_view, name='all_products'),
    path('cart/',cv.cart,name='cart'),
    path('add_cart/<int:product_id>/',cv.add_cart,name='add_cart'),
    path('remove_cart/<int:product_id>/',cv.remove_cart,name='remove_cart'),
    path('remove_cart_item/<int:product_id>/',cv.remove_cart_item,name='remove_cart_item'),
    path('search/',av.search,name="search"),
    path('payment_success/',pav.payment_success,name="payment_success"),
    path('payment_details_page/',pav.payment_details_page,name="payment_details_page"),
    path('add_to_wishlist/<int:product_id>',wv.add_to_wishlist,name="add_to_wishlist"),
    path('delete_from_wishlist/',wv.delete_from_wishlist,name="delete_from_wishlist"),
    path('wishlist/',wv.WishlistView,name='wishlist'),
    path('help_center/',av.help_center,name='help_center'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
