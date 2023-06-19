from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.core.mail import send_mail

from listings.models import Band
from listings.forms import BandForm
from listings.forms import ContactUsForm

test = [
    '<a href="../accueil/">Accueil</a>',
    '<a href="../studios/">Studios</a>',
    '<a href="../concert/">Concert</a>',
    '<a href="../bar/">Bar</a>',
    '<a href="../shop/">Shop</a>',
    '<a href="../programmation/">Programmation</a>',
    '<a href="../espace_pro/">Espace Pro</a>',
    '<a href="../contact/">Contact</a>',
]

test_url = ''
for url in test:
    test_url += '<li>' + url + '</li>'

def test(request):
    return render(request, 'listings/test.html')

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

def about(request):
    return HttpResponse('<h1>About Us</h1> <p>We love merch!</p>')

def accueil(request):
    return HttpResponse(test_url)

def studios(request):
    return HttpResponse(test_url)

def concert(request):
    return HttpResponse(test_url)

def bar(request):
    return HttpResponse(test_url)

def shop(request):
    return HttpResponse(test_url)

def programmation(request):
    return HttpResponse(test_url)

def espace_pro(request):
    return HttpResponse(test_url)

