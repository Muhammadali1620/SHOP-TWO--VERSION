from typing import Any
from django.core.management import BaseCommand
from apps.carts.models import Cart


class Command(BaseCommand): 
    def handle(self, *args, **options):
        last = Cart.objects.all().order_by('-pk').first()
        objs = [Cart(user_id=i, ProductFeature_id=i, counts=1)
            for i in range(last.pk + 1 if last else 1, last.pk + 102 if last else 101)
        ]
        Cart.objects.bulk_create(objs)
        self.stdout.write(self.style.SUCCESS(f'{Cart.objects.count()} cart created'))