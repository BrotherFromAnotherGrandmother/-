import os

import django
from django.utils.timezone import localtime

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')
django.setup()

from datacenter.models import Passcard, Visit  # noqa: E402

if __name__ == '__main__':
    print('Активных пропусков', len(Passcard.objects.filter(is_active=True)))
    print('Всего пропусков', Passcard.objects.count(), '\n')  # noqa: T001
    visiters_now = Visit.objects.filter(leaved_at=None)  # люди которые не ушли из хранилища
    for visiter in visiters_now:
        print(visiter.passcard.owner_name)
        print(f'Зашёл в хранилище, время по Москве:\n{localtime(visiter.entered_at)}')
        print(f'Находится в хранилище:\n{localtime() - localtime(visiter.entered_at)}\n')
    passcard = Passcard.objects.all()[54]
    visit_by_this_passcard = Visit.objects.filter(passcard=passcard)
    print(visit_by_this_passcard)

