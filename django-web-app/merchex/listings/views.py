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

def band_list(request):
    bands = Band.objects.all()
    return render(request, 'listings/band_list.html', {'bands': bands})

def band_detail(request, band_id):
    band = Band.objects.get(id=band_id)
    return render(request, 'listings/band_detail.html', {'band': band})
    # return render(request, 'listings/band_detail.html', {'id': band_id})

def band_create(request):
    form = BandForm()
    return render(request, 'listings/band_create.html', {'form': form})

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

