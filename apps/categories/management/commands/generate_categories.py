from typing import Any
from django.core.management import BaseCommand
from apps.categories.models import MainCategory, SubCategory
 

class Command(BaseCommand):
    def handle(self, *args, **options):
        lst = [
            MainCategory(name_uz = 'Kiyim', 
                        name_ru='Одежда', 
                        slug=f'kiym'),
            MainCategory(name_uz = 'Texnika', 
                        name_ru='Технтка', 
                        slug=f'texnik'),
            MainCategory(name_uz = 'Mebel', 
                        name_ru='Мебель', 
                        slug=f'mebel'),
        ]
        MainCategory.objects.bulk_create(lst)
        self.stdout.write(self.style.SUCCESS(f'{MainCategory.objects.count()} maincategory created'))

        lst = [
            SubCategory(main_category_id=1,
                        name_uz = 'Kofta', 
                        name_ru='Кофта', 
                        slug=f'kofta'),
            SubCategory(main_category_id=1,
                        name_uz = 'Oyoq kiyim', 
                        name_ru='Обувь', 
                        slug=f'oyoq'),
            SubCategory(main_category_id=1,
                        name_uz = 'Shim', 
                        name_ru='Брюки', 
                        slug=f'shim'),

            SubCategory(main_category_id=2,
                        name_uz = 'PC', 
                        name_ru='ПС', 
                        slug=f'pc'),
            SubCategory(main_category_id=2,
                        name_uz = 'Telefon', 
                        name_ru='Телефон', 
                        slug=f'tell'),
            SubCategory(main_category_id=2,
                        name_uz = 'Botovoy', 
                        name_ru='Ботовая', 
                        slug=f'botovoy'),

            SubCategory(main_category_id=3,
                        name_uz = 'Oshxona', 
                        name_ru='Кухня', 
                        slug=f'oshxona'),
            SubCategory(main_category_id=3,
                        name_uz = 'Mexmonxona', 
                        name_ru='Зал', 
                        slug=f'zal'),
            SubCategory(main_category_id=3,
                        name_uz = 'Spalni', 
                        name_ru='Спальня', 
                        slug=f'spalni'),
        ]
        SubCategory.objects.bulk_create(lst)
        self.stdout.write(self.style.SUCCESS(f'{SubCategory.objects.count()} subcategory created'))







        # last = MainCategory.objects.all().order_by('-pk').first()
        # maincategory = [MainCategory(name_uz = f'Main category NO {i}', 
        #                  name_ru=f'Main category NO {i}. ru', 
        #                  slug=f'main-category-no-{i}')
        #     for i in range(last.pk + 1 if last else 1, last.pk + 102 if last else 101)
        # ]
        # MainCategory.objects.bulk_create(maincategory)
        # self.stdout.write(self.style.SUCCESS(f'{MainCategory.objects.count()} maincategory created')) 

        # subcategory = [SubCategory(main_category_id=main.pk, 
        #                 name_uz=f'Sub category NO {i}', 
        #                 name_ru = f'sub-category-no-{i}ru', 
        #                 slug = f'sub-category-{main}-no-{i}')
        #     for i in range(1, 4)
        #     for main in MainCategory.objects.all()
        # ]
        # SubCategory.objects.bulk_create(subcategory)
        # self.stdout.write(self.style.SUCCESS(f'{MainCategory.objects.count()} subcategory created')) 