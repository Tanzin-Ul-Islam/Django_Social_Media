from django.contrib import admin
from django.urls import path
from login_app import views

app_name = 'login_app'

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', views.userlogin, name='login'),
    path('profile/', views.profile, name='profile'),
    path('edit_profile/', views.edit_profile, name='edit_profile'),
    path('author/<str:username>/', views.authors, name='authors'),
    path('follow/<str:username>/', views.followed, name='follow'),
    path('unfollow/<str:username>/', views.unfollowed, name='unfollow'),
    path('logout/', views.user_logout, name='logout'),

]