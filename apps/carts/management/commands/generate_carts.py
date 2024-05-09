from typing import Any
from django.core.management import BaseCommand
from apps.carts.models import Cart
from apps.features.models import ProductFeature


class Command(BaseCommand): 
    def handle(self, *args, **options):
        last = Cart.objects.all().order_by('-pk').first()
        objs = [Cart(user_id=i, productfeature=feture, counts=1)
            for i in range(1, 4)
            for feture in ProductFeature.objects.all()
        ]
        Cart.objects.bulk_create(objs)
        self.stdout.write(self.style.SUCCESS(f'{Cart.objects.count()} cart created'))