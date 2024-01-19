from django.shortcuts import redirect, render
from django.http import JsonResponse
import openai
import os
from django.contrib import auth
from django.contrib.auth.models import User
from .models import Chat
from django.utils import timezone

openai.api_key = os.environ.get('OPENAI_API_KEY', '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')

def ask_openai(message):
    """
    Sends a message to the OpenAI GPT-3.5-turbo model and retrieves a response.

    Parameters:
        message (str): The user's message to be sent to the AI model.

    Returns:
        str: The AI-generated response.

    Raises:
        Exception: If an error occurs during the OpenAI API request.
    """
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": message},
            ],
            max_tokens=400,
            n=1,
            stop=None,
            temperature=0.7,
        )
        answer = response.choices[0].message['content'].strip()
        return answer if answer else "No response from the AI."
    except Exception as e:
        return f"An error occurred: {str(e)}"

def chatboot(request):
    """
    Handles the chatbot functionality, including sending user messages to OpenAI and saving chat history.

    GET Request:
        Renders the 'chatboot.html' template with existing chat history for the authenticated user.

    POST Request:
        Receives a user's message, sends it to OpenAI, saves the chat history, and returns a JsonResponse with the message and response.

    Parameters:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: Renders 'chatboot.html' template for GET requests. Returns a JsonResponse for successful POST requests.

    Example:
        To send a message to the chatbot and receive a response:
        ```
        POST /chatboot/
        data: {'message': 'Hello, chatbot!'}
        ```
    """
    chats = Chat.objects.filter(user=request.user)

    if request.method == 'POST':
        message = request.POST.get('message')
        response = ask_openai(message)

        chat = Chat(user=request.user, message=message, response=response, created_at=timezone.now())
        chat.save()
        return JsonResponse({'message': message, 'response': response})
    return render(request, 'chatboot.html', {'chats': chats})

def login(request):
    """
    Handles user login functionality.

    POST Request:
        Attempts to authenticate the user with the provided username and password.
        On success, logs in the user and redirects to the 'chatboot' view.
        On failure, displays an error message on the 'login.html' template.

    Parameters:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: Renders 'login.html' template for GET requests. Redirects to 'chatboot' view on successful login.
    """
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('chatboot')
        else:
            error_message = 'Invalid username or password'
            return render(request, 'login.html', {'error_message': error_message})
    else:
        return render(request, 'login.html')

def register(request):
    """
    Handles user registration functionality.

    POST Request:
        Creates a new user with the provided username, email, and password.
        On success, logs in the new user and redirects to the 'chatboot' view.
        On failure, displays an error message on the 'register.html' template.

    Parameters:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: Renders 'register.html' template for GET requests. Redirects to 'chatboot' view on successful registration.
    """
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 == password2:
            try:
                user = User.objects.create_user(username, email, password1)
                user.save()
                auth.login(request, user)
                return redirect('chatboot')
            except:
                error_message = 'Error creating account'
                return render(request, 'register.html', {'error_message': error_message})
        else:
            error_message = 'Password don\'t match'
            return render(request, 'register.html', {'error_message': error_message})
    return render(request, 'register.html')

def logout(request):
    """
    Logs out the currently authenticated user.

    Parameters:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: Redirects to the 'login' view after successful logout.
    """
    auth.logout(request)
    return redirect('login')
