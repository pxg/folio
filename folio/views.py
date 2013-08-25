from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext

from folio.models import Project, Copy
from pprint import pprint


def index(request):
    projects = Project.objects.all()

    # TODO: make function
    # TODO: find smarter way to do this on each request (middlewear?)
    # could this be in a manager too?
    copy = Copy.objects.all()
    copy_dict = {}
    for item in copy:
        copy_dict[item.key] = item.value
    pprint(copy_dict)

    return render_to_response(
        'index.html',
        {'projects': projects, 'copy': copy_dict},
        context_instance=RequestContext(request))


def contact(request):
    return render_to_response('contact.html',
                              context_instance=RequestContext(request))


def detail(request, slug):
    project = get_object_or_404(Project, slug=slug)
    return render_to_response('detail.html', {'project': project},
                              context_instance=RequestContext(request))