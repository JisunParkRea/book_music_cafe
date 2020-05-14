from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from .searchBook import title_list, subtitle_list, book_img_src
from .searchMusic import name, artists, cover_img
from .searchAPI import search_local_cafe


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
        'name': name,
        'artists': artists,
        'cover_img': cover_img,
    }
    return HttpResponse(template.render(context, request))


def cafe_list(request):
    template = loader.get_template('book/cafe_list.html')

    cafe_list = []
    search_key = request.GET.get('search_key') # 검색어 가져오기
    if search_key: # 만약 검색어가 존재하면
        cafe_list = search_local_cafe(search_key)

    cafe_title = []
    cafe_addr = []
    cafe_link = []
    for cafe in cafe_list:
        cafe_title.append(cafe['title'])
        cafe_addr.append(cafe['address'])
        cafe_link.append(cafe['link'])

    context = {
        'cafe_title': cafe_title,
        'cafe_addr': cafe_addr,
        'cafe_link': cafe_link,
    }
    return HttpResponse(template.render(context, request))