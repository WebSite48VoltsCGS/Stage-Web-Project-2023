from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.core.mail import send_mail

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

def account(request):
    return render(request, 'listings/account.html')

def sign_in(request):
    return render(request, 'listings/signin.html')

def sign_up(request):
    return render(request, 'listings/base/signup.html')



"""
from listings.models import Band
from listings.forms import BandForm
from listings.forms import ContactUsForm

def band_list(request):
    bands = Band.objects.all()
    return render(request, 'listings/band_list.html', {'bands': bands})

def band_detail(request, band_id):
    band = Band.objects.get(id=band_id)
    return render(request, 'listings/band_detail.html', {'band': band})

def band_create(request):
    if request.method == 'POST':
        form = BandForm(request.POST)
        if form.is_valid():
            # Create a new 'Band' and save it to the database
            band = form.save()

            # Redirect to the detail page of the band we just created
            return redirect('band-detail', band.id)
    else:
        form = BandForm()
    return render(request, 'listings/band_create.html', {'form': form})

def band_delete(request, band_id):
    band = Band.objects.get(id=band_id)

    if request.method == 'POST':
        # delete the band from the database
        band.delete()
        # redirect to the bands list
        return redirect('band-list')

    # no need for an `else` here. If it's a GET request, just continue

    return render(request, 'listings/band_delete.html', {'band': band})

def band_change(request, band_id):
    band = Band.objects.get(id=band_id)
    if request.method == 'POST':
        form = BandForm(request.POST, instance=band)
        if form.is_valid():
            # Update the existing 'Band' in the database
            form.save()
            # Redirect to the detail page of the band we just updated
            return redirect('band-detail', band.id)
    else:
        form = BandForm(instance=band)
    return render(request, 'listings/band_change.html', {'form': form})

def contact(request):
    if request.method == 'POST':
        form = ContactUsForm(request.POST)
        # If the form is not valid, continue to the return
        # and display the form again (with errors).
        if form.is_valid():
            send_mail(
                subject=f'Message from {form.cleaned_data["name"] or "anonymous"} via MerchEx Contact Us form',
                message=form.cleaned_data['message'],
                from_email=form.cleaned_data['email'],
                recipient_list=['admin@merchex.xyz'])
            # When the email is sent, redirect to the following url
            return redirect('contact')
    else:
        form = ContactUsForm()
    return render(request, 'listings/contact.html', {'form': form})
"""
