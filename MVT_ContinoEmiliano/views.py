
from django.http import HttpResponse
from django.template import context, loader

def hola(request):
    return HttpResponse("<h1> SARASA </h1>")

def mi_template(request):
    template = loader.get_template('mi_template.html')
    template_renderizado = template.render()
    return HttpResponse(template_renderizado)