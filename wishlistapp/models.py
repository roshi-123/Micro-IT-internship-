from django.db import models
from cobalt_app.models import Product
from django.contrib.auth.models import User
# Create your models here.
class WishItem(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    def __str__(self):
        return self.product
    