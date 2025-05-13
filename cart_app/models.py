from django.db import models
from django.contrib.auth.models import User
from cobalt_app.models import Product

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='cart', unique=False)  # link cart to user
    cart_id = models.CharField(max_length=250, blank=True)
    date_added = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"Cart {self.cart_id} for {self.user.username}"

class CartItem_View(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    is_active = models.BooleanField(default=True)

    def sub_total(self):
        return self.product.new_price * self.quantity

    def __str__(self):
        return f"{self.product} in cart {self.cart.cart_id}"
