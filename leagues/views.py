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
		"ASC_teams": Team.objects.filter(league__name="Atlantic Soccer Conference"),
		"current_penguins": Team.objects.get(team_name="Penguins").curr_players.all(),
		"ICBC_teams": Team.objects.filter(league__name="International Collegiate Baseball Conference"),
		"ACAF_current": Player.objects.filter(Q(curr_team__league__name="American Conference of Amateur Football") & Q(last_name="Lopez")),
		"football_players": Player.objects.filter(curr_team__league__sport="Football"),
		"teams_with_sophia": Team.objects.filter(curr_players__first_name="Sophia"),
		"leagues_with_sophia": League.objects.filter(teams__curr_players__first_name="Sophia"),
		"flores_not_roughrider": Player.objects.filter(Q(last_name="Flores") & ~Q(curr_team__team_name="Roughriders")),
		"all_samuel_evans_teams": Team.objects.filter(Q(all_players__first_name__icontains="Samuel") & Q(all_players__last_name__icontains="Evans")),
		"all_players_manitoba": Player.objects.filter(all_teams__team_name__icontains="Tiger-Cats"),
		"former_vikings": Player.objects.filter(Q(all_teams__team_name="Vikings") & ~Q(curr_team__team_name="Vikings")),
		"jacob_gray_former": Team.objects.filter(Q(all_players__first_name="Jacob") & Q(all_players__last_name="Gray")),
		"AFABP_joshua": Player.objects.filter(first_name="Joshua").filter(all_teams__league__name="Atlantic Federation of Amateur Baseball Players"),
	}
	return render(request, "leagues/index.html", context)

def make_data(request):
	team_maker.gen_leagues(10)
	team_maker.gen_teams(50)
	team_maker.gen_players(200)

	return redirect("index")
