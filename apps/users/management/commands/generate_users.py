from django.core.management import BaseCommand
from apps.users.models import CustomUser


class Command(BaseCommand): 
    def handle(self, *args, **options):
        last = CustomUser.objects.all().order_by('-pk').first()
        users = [CustomUser(email=f'muhammadvalievmuhammadali{i}@gmail.com', 
                                 password=f'admin1620{i}')
            for i in range(last.pk + 1 if last else 1, last.pk + 102 if last else 101)
        ]
        CustomUser.objects.bulk_create(users)
        self.stdout.write(self.style.SUCCESS(f'{CustomUser.objects.count()} users created'))