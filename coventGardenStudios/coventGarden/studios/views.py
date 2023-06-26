from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.core.mail import send_mail
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

from studios.forms import SignUpForm
from studios.forms import SignInForm
from studios.forms import UserPasswordResetForm

"""
WIP
    - Placeholder
"""
def placeholder(request):
    return render(request, 'navigation/home.html')


"""
Navigation
    - Home
    - News
    - Studios
    - Bar
    - Pro area
    - Contact
    - Booking
"""
def home(request):
    return render(request, 'navigation/home.html')

def news(request):
    return render(request, 'navigation/news.html')

def studios(request):
    return render(request, 'navigation/studios.html')

def bar(request):
    return render(request, 'navigation/bar.html')

def pro_area(request):
    return render(request, 'navigation/pro_area.html')

def contact(request):
    return render(request, 'navigation/contact.html')

def booking(request):
    return render(request, 'navigation/booking.html')

"""
Account
    - Sign in
    - Sign out
    - Log out
"""
def account_sign_in(request):
    if request.method == 'POST':
        form = SignInForm(request.POST)
        if form.is_valid():
            # Log in the user
            username = request.POST["username"]
            password = request.POST["password"]
            account_log_in(request, username, password)

    # Return an empty form if GET request or form is invalid
    form = SignInForm()
    return render(request, 'account/account_sign_in.html', {'form': form})

def account_sign_up(request):
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
                # Create a new user
                user = User.objects.create_user(username, email, password)
                user.first_name = first_name
                user.last_name = last_name
                user.save()

                # Log in the user
                account_log_in(request, username, password)

    # Return an empty form if GET request or form is invalid
    form = SignUpForm()
    return render(request, 'account/account_sign_up.html', {'form': form})

def account_log_in(request, username, password):
    # Authenticate the user
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
    else:
        print("Error: A user is already logged in.")
    return redirect('profile_detail')

def account_log_out(request):
    logout(request)
    return redirect('account_sign_in')

"""
Profile
    - Detail
    - Update
    - Username update
    - Email update
    - Password update
"""
def profile_detail(request):
    return render(request, 'navigation/home.html')

def profile_update(request):
    return render(request, 'navigation/home.html')

def profile_username_update(request):
    return render(request, 'navigation/home.html')

def profile_email_update(request):
    return render(request, 'navigation/home.html')

def profile_password_update(request):
    return render(request, 'navigation/home.html')

"""
Groups
    - Detail
    - Create
    - Update
    - Delete
"""
def groups_detail(request):
    return render(request, 'navigation/home.html')

def groups_create(request):
    return render(request, 'navigation/home.html')

def groups_update(request):
    return render(request, 'navigation/home.html')

def groups_delete(request):
    return render(request, 'navigation/home.html')

"""
Bookings
    - Detail
    - Create
"""
def bookings_detail(request):
    return render(request, 'navigation/home.html')

def bookings_create(request):
    return render(request, 'navigation/home.html')

"""
Password reset
    - Forgot: password_reset_forgot.html
    - Done: password_reset_done.html
    - Confirm: password_reset_confirm.html
    - Complete: password_reset_complete.html
"""
