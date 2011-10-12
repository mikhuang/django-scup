from django.http import HttpResponse
from django.template import loader, RequestContext
from materials.models import Material
from fiber.models import Page

# Create your views here.
def index(request):
  materials = Material.objects.all()

  fiber_page = Page.objects.get(url__exact='materials')

  t = loader.get_template('materials.html')
  c = RequestContext(request, {
      'fiber_page': fiber_page,
      'materials': materials
  })
  return HttpResponse(t.render(c))