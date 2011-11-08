from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from django.template import loader, RequestContext
from tournaments.models import Tournament
from fiber.models import Page

# Create your views here.
def index(request):
  tournaments = Tournament.objects.all()

  fiber_page = _get_index_page();

  t = loader.get_template('index.html')
  c = RequestContext(request, {
      'fiber_page': fiber_page,
      'tournaments': tournaments
  })
  return HttpResponse(t.render(c))

def view_year(request, year):
  tournaments = Tournament.objects.all()

  fiber_page = _get_index_page();

  t = loader.get_template('view_year.html')
  c = RequestContext(request, {
      'fiber_page': fiber_page,
      'tournaments': tournaments
  })
  return HttpResponse(t.render(c))

def view_event(request, year, slug):
  tournament = get_object_or_404(Tournament, date__year=year, slug=slug)
  
  #tournament_page = _get_index_page()
  year_page = _get_year_page()
  page_name = slug

  try:
    fiber_page = Page.objects.get(url=page_name, parent=year_page)
  except:
    # if there is no page, just make it
    page = Page(
      url=page_name, 
      title="%s (%d)"%(tournament.name, tournament.date.year), 
      parent=year_page
    )
    fiber_page = page.save()

  t = loader.get_template('view_event.html')
  c = RequestContext(request, {
      'fiber_page': fiber_page,
      'tournament': tournament
  })
  return HttpResponse(t.render(c))

def _get_index_page():
  raise Exception
  
  try:
    fiber_page = Page.objects.get(absolute_url='/calendar/')
  except Page.DoesNotExist:
    return None

  return fiber_page

def _get_year_page(year):
  # try:
  #   Tournament.objects.filter(date__year=year)
  #   try:
  #     tournament_page = _get_index_page()
  #     fiber_page = Page.objects.get(url=year, parent=tournament_page)
  #   except:
  #     page = Page(url=year, parent=tournament_page, title="%d Tournaments"%year)
  #     fiber_page = page.save()

  #   return fiber_page
  # except:
  #   return None
  return None