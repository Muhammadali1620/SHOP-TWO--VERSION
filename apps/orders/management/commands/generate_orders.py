from typing import Any
from django.core.management import BaseCommand
from apps.orders.models import Order, OrderProduct
from apps.users.models import CustomUser
from apps.features.models import ProductFeature


class Command(BaseCommand):
    def handle(self, *args, **options):
        ordermodel = [Order(user_id=user.pk,
                            coupon_code=f'code cupon {i}',
                            payment_method_id=2,
                            total_price=2000 * i,
                            delivery_price=1000 * i,
                            coupon_price=100 * i,
                            is_paid=True, 
                            first_name=f'first_name No {i}',
                            last_name=f'last_name No {i}',
                            phone_number='+998994337104',
                            address1=f'address1 No {i}',
                            address2=f'address2 No {i}',
                            country=f'country No {i}',
                            region=f'region No {i}',
                            district=f'district No {i}',
                        )
            for i in range(1, 4)
            for user in CustomUser.objects.all()
        ]
        Order.objects.bulk_create(ordermodel)
        self.stdout.write(self.style.SUCCESS(f'{Order.objects.count()} ordermodel created'))

        orderproduct = [OrderProduct(product_feature_id=order.pk, counts=2, order_id=order.pk)
            for i in range(1, 4)
            for order in ProductFeature.objects.all()
        ]
        OrderProduct.objects.bulk_create(orderproduct)
        self.stdout.write(self.style.SUCCESS(f'{OrderProduct.objects.count()} orderproduct created'))