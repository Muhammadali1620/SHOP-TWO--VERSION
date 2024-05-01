from typing import Any
from django.core.management import BaseCommand
from apps.contacts.models import Contact


class Command(BaseCommand):
    def handle(self, *args, **options):
        last = Contact.objects.all().order_by('-pk').first()
        objs = [Contact(name=f'name No {i}', 
                        email=f'email No {i}', 
                        title=f'title No {i}', 
                        message=f'message No {i}')
            for i in range(last.pk + 1 if last else 1, last.pk + 102 if last else 101)
        ]
        Contact.objects.bulk_create(objs)
        self.stdout.write(self.style.SUCCESS(f'{Contact.objects.count()} contact created'))