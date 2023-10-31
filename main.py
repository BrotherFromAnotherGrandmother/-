import os

import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')
django.setup()

from datacenter.models import Passcard  # noqa: E402

if __name__ == '__main__':
    print(f'owner_name: {Passcard.objects.all()[8].owner_name}')
    print(f'passcode: {Passcard.objects.all()[8].passcode}')
    print(f'created_at: {Passcard.objects.all()[8].created_at}')
    print(f'is_active: {Passcard.objects.all()[8].is_active}')
    print('Количество пропусков:', Passcard.objects.count())  # noqa: T001
