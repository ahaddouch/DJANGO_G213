from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Chat(models.Model):
    """
    A Django model representing a chat message.

    Attributes:
        user (ForeignKey to User): The user who sent the message.
        message (TextField): The content of the message.
        response (TextField): The response to the message.
        created_at (DateTimeField): The timestamp when the chat was created (auto-generated).

    Methods:
        __str__(): Returns a string representation of the chat in the format 'username: message'.

    Example:
        chat_instance = Chat.objects.create(user=user_instance, message='Hello!', response='Hi there!')
        print(chat_instance)  # Output: 'username: Hello!'
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField()
    response = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.username}: {self.message}'