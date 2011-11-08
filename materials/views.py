from django.http import HttpResponse
from django.template import loader, RequestContext
from materials.models import Material
from fiber.models import Page

# Create your views here.
def index(request):
  materials = Material.objects.all()

  try:
    fiber_page = Page.objects.get(url__exact='/materials')
  except Page.DoesNotExist:
    # if there is no page, just make it
    page = Page(url='/materials', title="Materials")
    page.save()
    fiber_page = page

  t = loader.get_template('index.html')
  c = RequestContext(request, {
      'fiber_page': fiber_page,
      'materials': materials
  })
  return HttpResponse(t.render(c))