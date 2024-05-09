from typing import Any
from django.core.management import BaseCommand
from apps.products.models import Product


class Command(BaseCommand):
    def handle(self, *args, **options):
        lst = [
                Product(sub_category_id=1, 
                        title_uz="Fudbo'lka",
                        title_ru='Фудболка',
                        slug="fudbo'lka",
                        short_desc_uz="Vapshe zo'r fudbo'lka",
                        short_desc_ru='Вапще крутая фудболка',
                        long_desc_uz="Vapshe zo'r fudbo'lkaVapshe zo'r fudbo'lkaVapshe zo'r fudbo'lkaVapshe zo'r fudbo'lkaVapshe zo'r fudbo'lkaVapshe zo'r fudbo'lka",
                            long_desc_ru="Вапще крутая фудболкаВапще крутая фудболкаВапще крутая фудболкаВапще крутая фудболкаВапще крутая фудболкаВапще крутая фудболкаВапще крутая фудболка",),
    
                Product(sub_category_id=2, 
                        title_uz="Kraso'fka",
                        title_ru='Кросовка',
                        slug="krasofka",
                        short_desc_uz="Vapshe zo'r krasofka",
                        short_desc_ru='Вапще крутая красовка',
                        long_desc_uz="Vapshe zo'r krasofkaVapshe zo'r krasofkaVapshe zo'r krasofkaVapshe zo'r krasofkaVapshe zo'r krasofkaVapshe zo'r krasofkaVapshe zo'r krasofka",
                        long_desc_ru="Вапще крутая красовкаВапще крутая красовкаВапще крутая красовкаВапще крутая красовкаВапще крутая красовкаВапще крутая красовкаВапще крутая красовка",),
                
                Product(sub_category_id=3, 
                        title_uz="Jinsi shim",
                        title_ru='Джынсы',
                        slug="jinsi",
                        short_desc_uz="Vapshe zo'r Jinsi",
                        short_desc_ru='Вапще крутые Джынсы',
                        long_desc_uz="Vapshe zo'r JinsiVapshe zo'r JinsiVapshe zo'r JinsiVapshe zo'r JinsiVapshe zo'r JinsiVapshe zo'r JinsiVapshe zo'r JinsiVapshe zo'r Vapshe zo'r Jinsi",
                            long_desc_ru="Вапще крутая ДжынсыВапще крутая ДжынсыВапще крутая ДжынсыВапще крутая ДжынсыВапще крутая ДжынсыВапще крутая ДжынсыВапще крутая ДжынсыВапще крутая Джынсы",),
        
        
    
                Product(sub_category_id=4, 
                        title_uz="O'yin uchun kampyuter",
                        title_ru='Игровой компютер',
                        slug="oyinuchunkampyuter",
                        short_desc_uz="Vapshe zo'r kampyuter",
                        short_desc_ru='Вапще крутой компютер',
                        long_desc_uz="Vapshe zo'r kampyuterVapshe zo'r kampyuterVapshe zo'r kampyuterVapshe zo'r kampyuterVapshe zo'r kampyuterVapshe zo'r kampyuterVapshe zo'r kampyuter",
                            long_desc_ru="Вапще крутой компютерВапще крутой компютерВапще крутой компютерВапще крутой компютерВапще крутой компютерВапще крутой компютерВапще крутой компютер",),
    
                Product(sub_category_id=5,
                        title_uz="ASUS ROG PONE 8PRO",
                        title_ru='ASUS ROG PONE 8PRO',
                        slug="asusrogfon8pro",
                        short_desc_uz="Vapshe zo'r telefon, igrovoy",
                        short_desc_ru='Вапще крутой телефон, игровой ',
                        long_desc_uz="Vapshe zo'r telefon, igrovoyVapshe zo'r telefon, igrovoyVapshe zo'r telefon, igrovoyVapshe zo'r telefon, igrovoyVapshe zo'r telefon, igrovoyVapshe zo'r telefon, igrovoy",
                            long_desc_ru="Вапще крутой телефон, игровойВапще крутой телефон, игровойВапще крутой телефон, игровойВапще крутой телефон, игровойВапще крутой телефон, игровойВапще крутой телефон, игровой",),
    
                Product(sub_category_id=6, 
                        title_uz="Kir moshina",
                        title_ru='Стеральня машина',
                        slug="kirmoshina",
                        short_desc_uz="Vapshe zo'r kirm oshina",
                        short_desc_ru='Вапще крутая стералная машина',
                        long_desc_uz="Vapshe zo'r kirm oshinaVapshe zo'r kirm oshinaVapshe zo'r kirm oshinaVapshe zo'r kirm oshinaVapshe zo'r kirm oshinaVapshe zo'r kirm oshinaVapshe zo'r kirm oshinaVapshe zo'r kirm oshina",
                            long_desc_ru="Вапще крутая стералная машинаВапще крутая стералная машинаВапще крутая стералная машинаВапще крутая стералная машинаВапще крутая стералная машинаВапще крутая стералная машина",),
        
        
    
                Product(sub_category_id=7, 
                        title_uz="Oshxona mebeli",
                        title_ru='Кухонная мебель',
                        slug="oshxonmebel",
                        short_desc_uz="Vapshe zo'r Oshxona mebeli",
                        short_desc_ru='Вапще крутая Кухонная мебель',
                        long_desc_uz="Vapshe zo'r Oshxona mebeliVapshe zo'r Oshxona mebeliVapshe zo'r Oshxona mebeliVapshe zo'r Oshxona mebeliVapshe zo'r Oshxona mebeliVapshe zo'r Oshxona mebeliVapshe zo'r Oshxona mebeli",
                            long_desc_ru="Вапще крутая Кухонная мебельВапще крутая Кухонная мебельВапще крутая Кухонная мебельВапще крутая Кухонная мебельВапще крутая Кухонная мебельВапще крутая Кухонная мебельВапще крутая Кухонная мебель",),
    
                Product(sub_category_id=8, 
                        title_uz="Stol stullar",
                        title_ru='Стол и стулы',
                        slug="stolstul",
                        short_desc_uz="Vapshe zo'r Stol stullar",
                        short_desc_ru='Вапще крутая Стол и стулы',
                        long_desc_uz="Vapshe zo'r Stol stullarVapshe zo'r Stol stullarVapshe zo'r Stol stullarVapshe zo'r Stol stullarVapshe zo'r Stol stullarVapshe zo'r Stol stullarVapshe zo'r Stol stullarVapshe zo'r Stol stullar",
                            long_desc_ru="Вапще крутая Стол и стулыВапще крутая Стол и стулыВапще крутая Стол и стулыВапще крутая Стол и стулыВапще крутая Стол и стулыВапще крутая Стол и стулыВапще крутая Стол и стулыВапще крутая Стол и стулы",),
    
                Product(sub_category_id=9, 
                        title_uz="Kravta",
                        title_ru='Крвать',
                        slug="kravat",
                        short_desc_uz="Vapshe zo'r Kravta",
                        short_desc_ru='Вапще крутая Крвать',
                        long_desc_uz="Vapshe zo'r KravtaVapshe zo'r KravtaVapshe zo'r KravtaVapshe zo'r KravtaVapshe zo'r KravtaVapshe zo'r KravtaVapshe zo'r KravtaVapshe zo'r KravtaVapshe zo'r KravtaVapshe zo'r KravtaVapshe zo'r Kravta",
                        long_desc_ru="Вапще крутая КрватьВапще крутая КрватьВапще крутая КрватьВапще крутая КрватьВапще крутая КрватьВапще крутая КрватьВапще крутая КрватьВапще крутая КрватьВапще крутая КрватьВапще крутая КрватьВапще крутая Крвать",),
                ]
        Product.objects.bulk_create(lst)
        self.stdout.write(self.style.SUCCESS(f'{Product.objects.count()} product created'))


# class Command(BaseCommand):
#     def handle(self, *args, **options):
#         last = Product.objects.all().order_by('-pk').first()
#         product = [Product(sub_category_id=i%9+1, 
#                            title_uz=f'title_uz No {i}',
#                            title_ru=f'title_ru No {i}',
#                            slug=f'slug-no-{i}',
#                            short_desc_uz=f'short_desc_uz No {i}',
#                            short_desc_ru=f'short_desc_ru No {i}',
#                            long_desc_uz=f'long_desc_uz No {i}',
#                            long_desc_ru=f'long_desc_ru No {i}',)
#             for i in range(last.pk + 1 if last else 1, last.pk + 102 if last else 101)
#         ]
#         Product.objects.bulk_create(product)
#         self.stdout.write(self.style.SUCCESS(f'{Product.objects.count()} product created'))