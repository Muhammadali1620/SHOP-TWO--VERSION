from typing import Any
from django.core.management import BaseCommand
from apps.features.models import Feature, FeatureValue, ProductFeature


class Command(BaseCommand):
    def handle(self, *args, **options):
        last = Feature.objects.all().order_by('-pk').first()
        feature = [Feature(main_category_id=i if i % 2 == 0 else None,
                           sub_category_id=i if i % 2 != 0 else None,
                           ordering_number=i, 
                           name_uz=f'name_uz No {i}', 
                           slug=f'nameuz-no-{i}', 
                           name_ru=f'name_ru No {i}')
            for i in range(last.pk + 1 if last else 1, last.pk + 102 if last else 101)
        ]
        Feature.objects.bulk_create(feature)
        self.stdout.write(self.style.SUCCESS(f'{Feature.objects.count()} feature created'))

        featurevalue = [FeatureValue(feature_id=feature.pk, 
                                     value_uz=f'value_uz No {i}', 
                                     slug=f'valueuz-{feature}-no-{i}', 
                                     value_ru=f'value_ru No {i}')
            for i in range(1, 4)
            for feature in Feature.objects.all()
        ]
        FeatureValue.objects.bulk_create(featurevalue)
        self.stdout.write(self.style.SUCCESS(f'{FeatureValue.objects.count()} featurevalue created'))

        last = ProductFeature.objects.all().order_by('-pk').first()
        productfeature = [ProductFeature(product_id=i, 
                                         #feature_value_id=i,
                                         quantity=i, 
                                         price=1000 * i,
                                         )
            for i in range(last.pk + 1 if last else 1, last.pk + 102 if last else 101)
        ]
        ProductFeature.objects.bulk_create(productfeature)
        self.stdout.write(self.style.SUCCESS(f'{ProductFeature.objects.count()} productfeature created'))