# team/views.py
from django.shortcuts import render, get_object_or_404
from .models import Team, Player

def team(request):
    teams = Team.objects.all().order_by('id')  # 정렬 순서를 조정
    return render(request, 'team/team_list.html', {'team_list': teams})

def player_list(request, team_id):
    team = get_object_or_404(Team, id=team_id)
    players = Player.objects.filter(team=team)
    return render(request, 'team/player_list.html', {
        'team': team,
        'players': players
    })