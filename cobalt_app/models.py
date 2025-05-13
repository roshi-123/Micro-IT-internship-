from django.db import models

# Create your models here.
class Category(models.Model):
    name=models.CharField(max_length=50)
    def __str__(self):
        return self.name

class Product(models.Model):
    product_title=models.CharField(max_length=50)
    product_image=models.ImageField(upload_to="product")
    description=models.TextField()
    old_price=models.DecimalField(default=0,decimal_places=2,max_digits=10)
    new_price=models.DecimalField(default=0,decimal_places=2,max_digits=10)
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    is_featured=models.BooleanField(default=False)
    def __str__(self):
        return self.product_title

