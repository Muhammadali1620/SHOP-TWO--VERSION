from apps.carts.models import Cart
from apps.categories.models import MainCategory
from apps.general.models import General, SocialLink, PaymentMethod
from apps.wishlists.models import Wishlist


def general(request):
    user = request.user
    store_data = General.objects.first()
    categories = MainCategory.objects.all().order_by('pk')[0:12].prefetch_related('sub_cat')
    user_wishlist = Wishlist.objects.filter(user_id=user.pk).values_list('product_id', flat=True)
    user_cart_count = Cart.objects.filter(user_id=user.pk).count()
    sociallinks = SocialLink.objects.all()
    paymentmethods = PaymentMethod.objects.all()
    return {'store_data':store_data, 
            'categories':categories, 
            'user_wishlist':user_wishlist, 
            'sociallinks':sociallinks,
            'paymentmethods':paymentmethods,
            'user_cart_count':user_cart_count
            }
