from django.db import models

class Schedule(models.Model):
    month = models.IntegerField()
    date = models.IntegerField()
    day = models.CharField(max_length=10)
    time = models.CharField(max_length=10)
    stadium = models.CharField(max_length=20)
    team1 = models.CharField(max_length=20)
    team2 = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.month}/{self.date}({self.day}) {self.team1} vs {self.team2} - {self.stadium}"
