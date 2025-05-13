from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from .models import Product,Category
from django.db.models import Q

def registers(request):
    if request.method == "POST":
        # Handle user registration
        name = request.POST['register-name']
        email = request.POST['register-email']
        mobile = request.POST['register-mobile']
        password = request.POST['register-password']
        confirm_password = request.POST['register-confirm-password']
        
        # Check if the passwords match
        if password != confirm_password:
            return HttpResponse("Passwords do not match")  # Optionally return an error if passwords don't match
        
        # Check if the user with the same username or email already exists
        if User.objects.filter(username=name).exists():
            messages.error(request, "A user with this username already exists.")
            return redirect('register')  # Redirect back to the registration page
        
        if User.objects.filter(email=email).exists():
            messages.error(request, "A user with this email already exists.")
            return redirect('register')  # Redirect back to the registration page
        
        # Create a new user if the username and email are unique
        user = User.objects.create_user(username=name, email=email, password=password)
        user.save()
        
        messages.success(request, "Registration successful! You can now log in.")
        
        return redirect('login')  # Redirect to the login page

    # For GET requests, render the registration form
    return render(request, 'register.html')  # Assuming you have a template for the registration form


def logins(request):
    if request.method == "POST":
        login_name = request.POST['login-name']
        login_password = request.POST['login-password']
        
        # Authenticate the user
        user = authenticate(request, username=login_name, password=login_password)
        
        if user is not None:
            login(request, user)
            return redirect('index')  # Redirect to the index page
        else:
            # If authentication fails, show an error message
            messages.error(request, "Invalid username or password. Please try again.")
            return redirect('login')  # Redirect back to the login page
    
    # For GET requests, render the login form
    return render(request, "login.html")

def logout_view(request):
    logout(request)  # Logs the user out
    print("logout")
    return redirect('index')  # Redirect to the homepage or any other page after logging out

def product_view(request,pk):
    product=Product.objects.get(id=pk)
    return render(request,"product_view.html",{'product':product})
def category_view(request,pic):
    try:
        pic=pic.replace("-"," ")
        category=Category.objects.get(name=pic)
        product=Product.objects.filter(category=category)
        return render(request,"category_view.html",{'products':product,'category':category})
    except Exception:
        messages.success(request,"Category doesnt exist..")
def all_products_view(request):
    # Assuming 'Product' is your model for all products
    products = Product.objects.all()  # Get all products
    return render(request, 'all_products.html', {'products': products})

def search(request):
    if request.method=="POST":
        searched=request.POST['searched']
        searched=Product.objects.filter(Q(product_title__icontains=searched) | Q(description__icontains=searched))
        if not searched:
            return render(request,"search.html")
        else:
            return render(request,"search.html",{'searched':searched})
    else:
        return render(request,"search.html")
def help_center(request):
    return render(request,"help_center.html")