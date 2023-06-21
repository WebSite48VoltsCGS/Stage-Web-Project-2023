from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.core.mail import send_mail
from django.contrib.auth import authenticate, login

from listings.models import Account
from listings.forms import AccountForm
from listings.forms import SignForm

def home(request):
    return render(request, 'listings/home.html')

def news(request):
    return render(request, 'listings/news.html')

def studios(request):
    return render(request, 'listings/studios.html')

def bar(request):
    return render(request, 'listings/bar.html')

def pro_area(request):
    return render(request, 'listings/pro_area.html')

def contact(request):
    return render(request, 'listings/contact.html')

def booking(request):
    return render(request, 'listings/booking.html')

def account_detail(request, account_id):
    account = Account.objects.get(id=account_id)
    return render(request, 'listings/account_detail.html', {'account': account})

def sign_in(request):
    if request.method == 'POST':
        form = SignForm(request.POST)
        if form.is_valid():
            username = request.POST["username"]
            password = request.POST["password"]
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                # Redirect to a success page.
                return redirect('home')
            else:
                # Return an 'invalid login' error message.
                form = SignForm()
                return render(request, 'listings/signin.html', {'form': form})
    else:
        form = SignForm()
    return render(request, 'listings/signin.html', {'form': form})

def sign_up(request):
    if request.method == 'POST':
        form = AccountForm(request.POST)
        if form.is_valid():
            # Create a new 'account' and save it to the database
            account = form.save()

            # Redirect to the detail page of the 'account' we just created
            return redirect('account-detail', account.id)
    else:
        form = AccountForm()
    return render(request, 'listings/signup.html', {'form': form})
