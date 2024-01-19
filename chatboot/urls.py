from django.urls import path
from . import views
"""
    Django URL patterns for the chat application.

    - Register: Maps to the 'register' view for user registration.
    - Chatbot: Maps to the 'chatboot' view for handling chatbot functionality.
    - Login: Maps to the 'login' view for user login.
    - Logout: Maps to the 'logout' view for user logout.

    Example:
    To access the chatbot functionality, visit '/index' in the browser.

    urlpatterns = [
        path('', views.register, name='register'),
        path('index', views.chatboot, name='chatboot'),
        path('login', views.login, name='login'),
        path('logout', views.logout, name='logout'),
    ]
    """
urlpatterns = [
    
    path('', views.register, name='register'),
    path('index', views.chatboot, name='chatboot'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
  

]