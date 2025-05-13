from django.shortcuts import render
from cobalt_app.models import Product
# Create your views here.
def indexs(request):
    product=Product.objects.filter(is_featured=True)
    return render(request,"index.html",{'products':product})
