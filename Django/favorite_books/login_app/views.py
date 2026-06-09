from django.shortcuts import redirect, render
from django.http import JsonResponse
from .models import User
from django.contrib import messages
from django.contrib.messages import get_messages

def login(request):
    if request.method == 'POST':
        errors, user = User.objects.authenticate(request.POST['email'], request.POST['password'])

        if errors:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect('login')

        if user:
            request.session['user_id'] = user.id
            return redirect('books:create_book')

    return render(request, 'login.html')


def register(request):
    if request.method == 'POST':
        errors = User.objects.validate_registration(request.POST)


        if errors:
            for key, value in errors.items():
                messages.error(request, value)
            # Send old data inputs to the template to pre-fill the form
            return render(request, 'register.html', {
                'old_data': request.POST
            })
        else:
            user = User.objects.create_user(request.POST)
            request.session['user_id'] = user.id
            # Redirect to messages_list url in books app
            return redirect('books:create_book')

    # Clear the old messages
    storage = get_messages(request)
    for message in storage:
        pass

    return render(request, 'register.html')


def check_email(request):
    email = request.GET.get('email', '').strip()
    exists = False

    if email:
        exists = User.objects.filter(email=email).exists()

    return JsonResponse({'email': email, 'exists': exists})


def logout(request):
    if request.method == 'POST':
        request.session.flush()
        return redirect('login')
