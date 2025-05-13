from django.shortcuts import render,reverse,redirect, get_object_or_404
from .models import WishItem
from cobalt_app.models import Product
from django.http import HttpResponseRedirect
from django.contrib import messages
# Create your views here.
def WishlistView(request):
    wish_items=WishItem.objects.filter(user=request.user)
    return render(request,'wishlist.html',{'wish_items':wish_items})
def add_to_wishlist(request, product_id):
    # Check if the user is authenticated
    if not request.user.is_authenticated:
        # Display a message to the user to log in
        messages.error(request, "You need to log in to add items to your wishlist.")
        return redirect('index')  # Redirect to the login page (or adjust as needed)

    # Fetch the product or return 404 if not found
    product = get_object_or_404(Product, id=product_id)

    # Try to get the WishItem, or create it if it doesn't exist
    try:
        wishlist_item = WishItem.objects.get(product=product, user=request.user)
    except WishItem.DoesNotExist:
        wishlist_item = WishItem.objects.create(product=product, user=request.user)

    # Save the wishlist item
    wishlist_item.save()

    # Redirect to the wishlist page (adjust as needed)
    return redirect('wishlist')


def delete_from_wishlist(request):
    if request.method == "POST":
        item_id = request.POST.get('item_id')  # Get the item_id from the form
        if item_id:
            # Delete the WishItem with the given item_id
            WishItem.objects.filter(id=item_id).delete()
        return HttpResponseRedirect(reverse('wishlist'))  # Redirect back to the wishlist page
    return HttpResponseRedirect(reverse('wishlist'))  # In case it's not a POST request