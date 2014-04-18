from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext


def home(request):
    return render(request, 'home/index.html', context_instance=RequestContext(request))
