from apps.categories.models import MainCategory
from apps.general.models import General


def general(request):
    sub_category_id = request.GET.get('sub_category', 0)
    return {'store_data': General.objects.first(), 'categories': MainCategory.objects.all().order_by('-pk')[0:12], 'sub_category_id':int(sub_category_id)}
