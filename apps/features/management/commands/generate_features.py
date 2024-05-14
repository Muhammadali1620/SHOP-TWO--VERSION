from typing import Any
from django.core.management import BaseCommand
from apps.products.models import Product
from apps.features.models import Feature, FeatureValue, ProductFeature


class Command(BaseCommand):
    def handle(self, *args, **options):
        lst = [
                Feature(main_category_id=1,
                        ordering_number=1, 
                        name_uz="O'lcham", 
                        slug='olcham',
                        name_ru='Размер'),

                Feature(main_category_id=2,
                        ordering_number=2, 
                        name_uz="RAM", 
                        slug='ram',
                        name_ru='ОЗУ'),

                Feature(main_category_id=3,
                        ordering_number=3, 
                        name_uz="Razmer", 
                        slug='razmer',
                        name_ru='Размер'),
        ]
        Feature.objects.bulk_create(lst)
        self.stdout.write(self.style.SUCCESS(f'{Feature.objects.count()} feature created'))

        lst = [
                FeatureValue(feature_id=1, 
                                      value_uz='L', 
                                      slug='l', 
                                      value_ru='L'),
                FeatureValue(feature_id=1, 
                                      value_uz='X', 
                                      slug='x', 
                                      value_ru='X'),
                FeatureValue(feature_id=1, 
                                      value_uz='XL', 
                                      slug='xl', 
                                      value_ru='XL'),
                
                FeatureValue(feature_id=2, 
                                      value_uz='8Gb', 
                                      slug='8gb', 
                                      value_ru='8Gb'),
                FeatureValue(feature_id=2, 
                                      value_uz='16Gb', 
                                      slug='16gb', 
                                      value_ru='16Gb'),
                FeatureValue(feature_id=2, 
                                      value_uz='24Gb', 
                                      slug='24gb', 
                                      value_ru='24Gb'),

                FeatureValue(feature_id=3, 
                                      value_uz='3m-1m', 
                                      slug='3m-1m', 
                                      value_ru='3m-1m'),
                FeatureValue(feature_id=3, 
                                      value_uz='4m-1,5m', 
                                      slug='4m-1-5m', 
                                      value_ru='4m-1,5m'),
                FeatureValue(feature_id=3, 
                                      value_uz='1,5m-1m', 
                                      slug='1-5m-1m', 
                                      value_ru='1,5m-1m'),
        ]
        FeatureValue.objects.bulk_create(lst)
        self.stdout.write(self.style.SUCCESS(f'{FeatureValue.objects.count()} feature value created'))



        # last = Feature.objects.all().order_by('-pk').first()
        # feature = [Feature(main_category_id=i if i % 2 == 0 else None,
        #                    sub_category_id=i if i % 2 != 0 else None,
        #                    ordering_number=i, 
        #                    name_uz=f'name_uz No {i}', 
        #                    slug=f'nameuz-no-{i}', 
        #                    name_ru=f'name_ru No {i}')
        #     for i in range(last.pk + 1 if last else 1, last.pk + 102 if last else 101)
        # ]
        # Feature.objects.bulk_create(feature)
        # self.stdout.write(self.style.SUCCESS(f'{Feature.objects.count()} feature created'))

        # featurevalue = [FeatureValue(feature_id=feature.pk, 
        #                              value_uz=f'value_uz No {i}', 
        #                              slug=f'valueuz-{feature.pk}-no-{i}', 
        #                              value_ru=f'value_ru No {i}')
        #     for i in range(1, 4)
        #     for feature in Feature.objects.all()
        # ]
        # FeatureValue.objects.bulk_create(featurevalue)
        # self.stdout.write(self.style.SUCCESS(f'{FeatureValue.objects.count()} featurevalue created'))

        last = ProductFeature.objects.all().order_by('-pk').first()
        productfeature = [ProductFeature(product_id=product.pk, 
                                         #feature_value_id=i,
                                         quantity=i, 
                                         price=1000 * product.pk,
                                         )
            for i in range(1,4)
            for product in  Product.objects.all()
        ]
        ProductFeature.objects.bulk_create(productfeature)
        self.stdout.write(self.style.SUCCESS(f'{ProductFeature.objects.count()} productfeature created'))