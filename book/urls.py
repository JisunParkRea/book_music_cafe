from django.conf.urls import url 
from . import views
 
urlpatterns = [
    url('home/', views.index, name='index'),
    url('book/', views.book_list, name='book_list'),
    url('music/', views.music_list, name='music_list'),
    url('cafe/', views.cafe_list, name='cafe_list'),
]