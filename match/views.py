from django.shortcuts import render
from .models import Schedule

def schedule_list(request):
    schedules = Schedule.objects.all().order_by('month', 'day', 'time')
    context = {
        'schedules': schedules
    }
    return render(request, 'match/schedule_list.html', context)
