from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader


def index(request):
    template = loader.get_template('book/index.html')
    context = {
        'test': "test"
    }
    return HttpResponse(template.render(context, request))