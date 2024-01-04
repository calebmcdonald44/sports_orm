from django.shortcuts import render, redirect
from .models import League, Team, Player
from django.db.models import Q
from . import team_maker

def index(request):
	context = {
		"leagues": League.objects.all(),
		"teams": Team.objects.all(),
		"players": Player.objects.all(),
		"baseball_leagues": League.objects.filter(sport='Baseball'),
		"women_leagues": League.objects.filter(name__icontains="Women"),
		"hockey_leagues": League.objects.filter(sport__icontains="Hockey"),
		"not_football_leagues": League.objects.exclude(sport="Football"),
		"conferences": League.objects.filter(name__icontains="Conference"),
		"atlantic_leagues": League.objects.filter(name__icontains="Atlantic"),
		"dallas_teams": Team.objects.filter(location="Dallas"),
		"raptors": Team.objects.filter(team_name="Raptors"),
		"includes_city": Team.objects.filter(location__icontains="City"),
		"starts_t": Team.objects.filter(team_name__istartswith="T"),
		"abc_location": Team.objects.order_by('location'),
		"reverse_abc_name": Team.objects.order_by('-team_name'),
		"cooper_last": Player.objects.filter(last_name="Cooper"),
		"joshua_first": Player.objects.filter(first_name="Joshua"),
		"alexander_or_wyatt": Player.objects.filter(Q(first_name="Alexander") | Q(first_name="Wyatt")),
	}
	return render(request, "leagues/index.html", context)

def make_data(request):
	team_maker.gen_leagues(10)
	team_maker.gen_teams(50)
	team_maker.gen_players(200)

	return redirect("index")