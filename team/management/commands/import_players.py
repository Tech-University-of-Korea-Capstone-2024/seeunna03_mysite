import csv
from django.core.management.base import BaseCommand
from team.models import Team, Player
from datetime import datetime
from django.conf import settings
import os

class Command(BaseCommand):
    help = 'Import players from CSV'

    def handle(self, *args, **kwargs):
        file_path = os.path.join(settings.BASE_DIR, 'baseball_data', 'player.csv')

        try:
            with open(file_path, newline='', encoding='utf-8') as f:
                reader = csv.DictReader(f)
                for row in reader:
                    team_id = row['team_id']
                    team, created = Team.objects.get_or_create(team_id=team_id)

                    birthday = datetime.strptime(row['birthday'], '%m/%d/%Y').date()

                    Player.objects.update_or_create(
                        player_id=row['player_id'],
                        defaults={
                            'backnumber': int(row['backnumber']) if row['backnumber'] else None,
                            'team': team,
                            'position': row['position'],
                            'birthday': birthday,  # 여기 수정됨!
                            'profile': row['profile'],
                            'school': row['school'],
                        }
                    )

            self.stdout.write(self.style.SUCCESS('✅ 선수 데이터를 성공적으로 가져왔습니다.'))

        except Exception as e:
            self.stderr.write(self.style.ERROR(f'❌ 오류 발생: {e}'))
