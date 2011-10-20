from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from django.template import loader, RequestContext
from tournaments.models import Tournament
from fiber.models import Page

# Create your views here.
def index(request):
  tournaments = Tournament.objects.all()

  try:
    fiber_page = Page.objects.get(url__exact='tournaments')
  except:
    # if there is no page, just make it
    page = Page(url='tournaments', title="Tournaments")
    fiber_page = page.save()

  t = loader.get_template('index.html')
  c = RequestContext(request, {
      'fiber_page': fiber_page,
      'tournaments': tournaments
  })
  return HttpResponse(t.render(c))

def view(request, year, slug):
  tournament = get_object_or_404(Tournament, date__year=year, slug=slug)
  
  page_name = 'tournament_' + str(tournament.id) #default name for a tournament's page

  try:
    fiber_page = Page.objects.get(url__exact=page_name)
  except:
    # if there is no page, just make it
    page = Page(url=page_name, title="%s (%d)"%(tournament.name, tournament.date.year))
    fiber_page = page.save()

  t = loader.get_template('view.html')
  c = RequestContext(request, {
      'fiber_page': fiber_page,
      'tournament': tournament
  })
  return HttpResponse(t.render(c))

  