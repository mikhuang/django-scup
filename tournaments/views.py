from django.shortcuts import get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.template import loader, RequestContext
from django.core.xheaders import populate_xheaders
from django.conf import settings
from django.core.urlresolvers import reverse

from tournaments.models import Tournament

from fiber.models import Page
from fiber.app_settings import DEFAULT_TEMPLATE

# Create your views here.
def index(request):
  # redirect to current year
  year = settings.TOURNAMENT_YEARS[0]
  return HttpResponseRedirect(reverse('tournaments.views.view_year', kwargs={'year':year}))
  #tournaments = Tournament.objects.all()
#
  #context, page = _get_content(request)
#
  #t = loader.get_template(page.template_name or 'index.html' or DEFAULT_TEMPLATE)
  #c = RequestContext(request, {
  #  'page': page,
  #  'tournaments': tournaments,
  #  'years': settings.TOURNAMENT_YEARS,
  #})
#
  #response = HttpResponse(t.render(c))
  #populate_xheaders(request, response, Page, page.id)
  #return response

def view_year(request, year):
  # check if year is valid
  try:
    year = int(year)
  except ValueError:
    raise Http404

  years = settings.TOURNAMENT_YEARS
  if not year in years:
    raise Http404

  # filter by YEAR
  tournaments = Tournament.objects.filter(date__year=year)

  try:
    context, page = _get_content(request)
  except Http404:
    url = reverse('tournaments.views.view_year', kwargs={'year':year})
    # look for this page under it's absolute url
    try:
      page = Page.objects.get(url=url)
    except Page.DoesNotExist:
      # we need to create this page
      page = Page(url=url, title="%d Tournaments"%year)
      page.save()
      
  t = loader.get_template(page.template_name or 'view_year.html' or DEFAULT_TEMPLATE)
  c = RequestContext(request, {
    'fiber_page': page,
    'year': year,
    'tournaments': tournaments,
    'years': years,
  })

  response = HttpResponse(t.render(c))
  populate_xheaders(request, response, Page, page.id)
  return response

def view_event(request, year, slug):
  tournament = get_object_or_404(Tournament, date__year=year, slug=slug)
  return _view_event(request, tournament)

def view_event_by_id(request, id):
  tournament = get_objects_or_404(Tournament, id=id)
  return _view_event(request, tournament)

def _view_event(request, tournament):
  try:
    context, page = _get_content(request)
  except Http404:
      url = tournament.get_absolute_url_by_id()
      # look for this page under it's absolute url
      try:
        page = Page.objects.get(url=url)
      except Page.DoesNotExist:
        # we need to create this page
        page = Page(url=url, title=str(tournament))
        page.save()
  
  t = loader.get_template(page.template_name or 'view_event.html' or DEFAULT_TEMPLATE)
  c = RequestContext(request, {
    'fiber_page': page,
    'tournament': tournament,
    'years': settings.TOURNAMENT_YEARS,
  })

  response = HttpResponse(t.render(c))
  populate_xheaders(request, response, Page, page.id)
  return response

def _get_content(request):
  context = RequestContext(request)
  if 'fiber_page' not in context:
      raise Http404
  else:
      page = context['fiber_page']

  return context, page

#def _get_years_of_tournaments():
#  tournaments = Tournament.objects.order_by('date')
#  first = tournaments[0]
#  last = tournaments.reverse()[0]



