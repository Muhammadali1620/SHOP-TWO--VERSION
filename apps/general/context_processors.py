from apps.categories.models import MainCategory
from apps.general.models import General
from apps.wishlists.models import Wishlist


def general(request):
    user_wishlist = Wishlist.objects.filter(user_id=request.user.pk).values_list('product_id', flat=True)
    return {'store_data': General.objects.first(), 'categories': MainCategory.objects.all().order_by('pk')[0:12], 'user_wishlist':user_wishlist}
