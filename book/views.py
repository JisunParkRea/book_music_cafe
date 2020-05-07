from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from .searchBest import title_list, subtitle_list, book_img_src


def index(request):
    template = loader.get_template('book/index.html')
    context = {
        'title_list': title_list,
        'subtitle_list': subtitle_list,
        'book_img_src': book_img_src,
    }
    return HttpResponse(template.render(context, request))