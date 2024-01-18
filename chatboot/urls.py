from django.urls import path
from . import views

urlpatterns = [
    
    path('', views.register, name='register'),
    path('index', views.chatboot, name='chatboot'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
  

]