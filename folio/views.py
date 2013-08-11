from django.shortcuts import render_to_response
from django.template import RequestContext

from folio.models import Project


def index(request):
    projects = Project.objects.all()
    return render_to_response('index.html', {'projects': projects},
                              context_instance=RequestContext(request))