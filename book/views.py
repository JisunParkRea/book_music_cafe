from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from .searchBook import title_list, subtitle_list, book_img_src


def index(request):
    template = loader.get_template('book/index.html')
    context = {
        'title_list': title_list,
    }
    return HttpResponse(template.render(context, request))


def book_list(request):
    template = loader.get_template('book/book_list.html')
    context = {
        'title_list': title_list,
        'subtitle_list': subtitle_list,
        'book_img_src': book_img_src,
    }
    return HttpResponse(template.render(context, request))


def music_list(request):
    template = loader.get_template('book/music_list.html')
    context = {
        'title_list': title_list,
    }
    return HttpResponse(template.render(context, request))


def cafe_list(request):
    template = loader.get_template('book/cafe_list.html')
    context = {
        'title_list': title_list,
    }
    return HttpResponse(template.render(context, request))