from django.db import models

class Team(models.Model):
    team_id = models.CharField(max_length=10, unique=True)  # 팀 ID (예: KIA)
    name = models.CharField(max_length=100)  # 팀 이름 (추후 추가 가능)
    logo = models.ImageField(upload_to='team_logos/', null=True, blank=True)  # 팀 로고 추가
    
    def __str__(self):
        return self.team_id


class Player(models.Model):
    backnumber = models.IntegerField(null=True, blank=True)  # 등번호
    player_id = models.CharField(max_length=50, unique=True)  # 선수 ID
    team = models.ForeignKey(Team, on_delete=models.CASCADE)  # 소속 팀 (ForeignKey)
    position = models.CharField(max_length=20)  # 포지션
    birthday = models.DateField()  # 생년월일
    profile = models.CharField(max_length=100)  # 신체 정보
    school = models.TextField()  # 학력

    def __str__(self):
        return f"{self.player_id} ({self.team.team_id})"
