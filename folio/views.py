from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext

from folio.models import Project


def index(request):
    projects = Project.objects.all()
    return render_to_response('index.html', {'projects': projects},
                              context_instance=RequestContext(request))


def contact(request):
    return render_to_response('contact.html',
                              context_instance=RequestContext(request))


def detail(request, project_id):
    project = get_object_or_404(Project, id=project_id)
    return render_to_response('detail.html', {'project': project},
                              context_instance=RequestContext(request))