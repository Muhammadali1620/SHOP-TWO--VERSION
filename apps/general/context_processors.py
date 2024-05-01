from apps.categories.models import MainCategory
from apps.general.models import General


def general(request):
    return {'store_data': General.objects.first(), 'categories': MainCategory.objects.all().order_by('pk')[0:12]}
