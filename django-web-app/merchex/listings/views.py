from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.core.mail import send_mail
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from listings.forms import SignUpForm
from listings.forms import SignInForm

def home(request):
    return render(request, 'home.html')

def news(request):
    return render(request, 'news.html')

def studios(request):
    return render(request, 'studios.html')

def bar(request):
    return render(request, 'bar.html')

def pro_area(request):
    return render(request, 'pro_area.html')

def contact(request):
    return render(request, 'contact.html')

def booking(request):
    return render(request, 'booking.html')

def account(request):
    return render(request, 'account.html')

def sign_in(request):
    if request.method == 'POST':
        form = SignInForm(request.POST)
        if form.is_valid():
            # Authenticate the user
            username = request.POST["username"]
            password = request.POST["password"]
            user = authenticate(request, username=username, password=password)

            # Successful login
            if user is not None:
                login(request, user)
                # Redirect to a success page.
                return redirect('home')

            # Invalid login errors
            else:
                # Return an 'invalid login' error message.
                pass

    # Return an empty form if GET request or login is invalid
    form = SignInForm()
    return render(request, 'registration/sign_in.html', {'form': form})

def sign_up(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            username = request.POST["username"]
            first_name = request.POST["first_name"]
            last_name = request.POST["last_name"]
            email = request.POST["email"]
            password = request.POST["password"]
            confirm_password = request.POST["confirm_password"]

            if password == confirm_password:
                user = User.objects.create_user(username, email, password)
                user.first_name = first_name
                user.last_name = last_name
                user.save()
                return redirect('home')
    form = SignUpForm()
    return render(request, 'registration/sign_up.html', {'form': form})
