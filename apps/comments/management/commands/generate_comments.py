from typing import Any
from django.core.management import BaseCommand
from apps.comments.models import Comment
from apps.products.models import Product

class Command(BaseCommand):
    def handle(self, *args, **options): 
        objs = [Comment(product_id=product.pk, 
                        user_id=product.pk,
                        name=f'Kimdur NO {i}', 
                        email=f'muhammadvalievmuhammadali{i}@gmail.com', 
                        message=f'message NO {i}', rating=5)
            for i in range(1, 4)
            for product in Product.objects.all()
        ]
        Comment.objects.bulk_create(objs)
        self.stdout.write(self.style.SUCCESS(f'{Comment.objects.count()} comment created'))