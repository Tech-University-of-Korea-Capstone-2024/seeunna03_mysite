import csv
from django.core.management.base import BaseCommand
from django.conf import settings
from match.models import Schedule

class Command(BaseCommand):
    help = 'Import schedule data from CSV'

    def handle(self, *args, **kwargs):
        file_path = settings.BASE_DIR / 'baseball_data' / 'schedule.csv'

        with open(file_path, newline='', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                schedule = Schedule(
                    month=int(row['month']),
                    date=int(row['date']),
                    day=row['day'],
                    time=row['time'],
                    stadium=row['stadium'],
                    team1=row['team1'],
                    team2=row['team2']
                )
                schedule.save()

        self.stdout.write(self.style.SUCCESS('✔ 스케줄 데이터가 성공적으로 저장되었습니다.'))


