import os 
from django.core.management import BaseCommand

class Command(BaseCommand):
    def handle(self, *args, **options):
        os.system('find . -path "*/migrations/0*" -delete')
        os.system('rm -rf db.sqlite3')