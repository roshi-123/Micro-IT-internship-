from wishlistapp.models import WishItem


def wishlist_counter(request):
    if request.user.is_authenticated:
        return {
                    'wish_count': WishItem.objects.filter(user=request.user).count()
            }
    else:
        return {
                    'wish_count': 0
        }
