from django.urls import path
from . import views

urlpatterns = [
    path('', views.chatboot, name='chatboot'),
    path('login', views.login, name='login'),
    path('register', views.register, name='register'),
    path('logout', views.logout, name='logout'),

]