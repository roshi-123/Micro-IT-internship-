from django.shortcuts import render, redirect, get_object_or_404
from cobalt_app.models import Product
from .models import Cart, CartItem_View
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from django.contrib import messages
# Helper function to get or create cart_id for guest
def _cart_id(request):
    cart = request.session.session_key
    if not cart:
        cart = request.session.create()
    return cart

def add_cart(request, product_id):
    product = Product.objects.get(id=product_id)
    
    # Check if the user is logged in or a guest
    user = request.user if request.user.is_authenticated else None

    if not user and not request.user.is_authenticated:
        # If the user is not logged in, show a message and redirect them to the login page
        messages.error(request, "You need to be logged in to add items to the cart.")
        return redirect('index')  
    
    try:
        # Attempt to get the cart for the current user (or guest)
        cart = Cart.objects.get(cart_id=_cart_id(request), user=user)
    except Cart.DoesNotExist:
        # If the cart doesn't exist, create a new one
        cart = Cart.objects.create(
            cart_id=_cart_id(request),
            user=user
        )
    cart.save()

    try:
        # Check if the product is already in the cart, and increase quantity if so
        cart_item = CartItem_View.objects.get(product=product, cart=cart)
        cart_item.quantity += 1
        cart_item.save()
    except CartItem_View.DoesNotExist:
        # If the product isn't in the cart, create a new cart item
        cart_item = CartItem_View.objects.create(
            product=product,
            quantity=1,
            cart=cart,
        )
        cart_item.save()
    return redirect('cart')

# Display the cart
def cart(request, total=0, quantity=0, cart_items=None):
    try:
        cart = Cart.objects.get(cart_id=_cart_id(request), user=request.user if request.user.is_authenticated else None)
        cart_items = CartItem_View.objects.filter(cart=cart, is_active=True)
        for cart_item in cart_items:
            total += (cart_item.product.new_price * cart_item.quantity)
            quantity += cart_item.quantity
    except Cart.DoesNotExist:
        pass  # No cart found for the user or guest session

    return render(request, 'cart.html', {'total': total, 'quantity': quantity, 'cart_items': cart_items})

# Remove a single quantity from the cart
def remove_cart(request, product_id):
    cart = Cart.objects.get(cart_id=_cart_id(request), user=request.user if request.user.is_authenticated else None)
    product = get_object_or_404(Product, id=product_id)
    cart_item = CartItem_View.objects.get(product=product, cart=cart)
    if cart_item.quantity > 1:
        cart_item.quantity -= 1
        cart_item.save()
    else:
        cart_item.delete()
    return redirect('cart')

# Remove the entire cart item
def remove_cart_item(request, product_id):
    cart = Cart.objects.get(cart_id=_cart_id(request), user=request.user if request.user.is_authenticated else None)
    product = get_object_or_404(Product, id=product_id)
    cart_item = CartItem_View.objects.get(product=product, cart=cart)
    cart_item.delete()
    return redirect('cart')


