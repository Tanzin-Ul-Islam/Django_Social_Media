from django.contrib import admin
from django.urls import path
from post_app import views

app_name = 'post_app'

urlpatterns = [
    path('', views.index, name='index'),
    path('createpost/', views.createpost, name='createpost'),
    path('like/<pk>/', views.liked, name='likes'),
    path('dislike/<pk>/', views.disliked, name='dislikes'),

]