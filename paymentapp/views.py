from django.shortcuts import render

# Create your views here.
def payment_success(request):
    return render(request,'payment_success.html')

def payment_details_page(request):
    return render(request,'payment_details_page.html')