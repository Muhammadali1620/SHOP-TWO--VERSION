import os 
from django.core.management import BaseCommand

class Command(BaseCommand):
    def handle(self, *args, **options):
        os.system('python manage.py makemigrations')
        os.system('python manage.py migrate')
        os.system('python manage.py generate_users')
        os.system('python manage.py generate_categories')
        os.system('python manage.py generate_contacts')
        os.system('python manage.py generate_products')
        os.system('python manage.py generate_generals')
        os.system('python manage.py generate_comments')
        os.system('python manage.py generate_features')
        os.system('python manage.py generate_carts')
        os.system('python manage.py generate_orders')