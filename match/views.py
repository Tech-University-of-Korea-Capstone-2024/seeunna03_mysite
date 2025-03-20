import csv
import os
from django.shortcuts import render
from django.conf import settings

def schedule_list(request):
    schedule_path = os.path.join(settings.BASE_DIR, "baseball_data", "schedule.csv")  # CSV 파일 경로
    schedules = []

    with open(schedule_path, newline="", encoding="utf-8") as csvfile:
        reader = csv.reader(csvfile)
        next(reader)
        for row in reader:
            schedules.append({
                "month": row[0],
                "day": row[1],
                "weekday": row[2],
                "time": row[3],
                "stadium": row[4],
                "team1": row[5],
                "team2": row[6],
            })

    return render(request, "match/schedule_list.html", {"schedules": schedules})