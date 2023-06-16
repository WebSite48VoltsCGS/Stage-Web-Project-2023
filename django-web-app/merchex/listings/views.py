from django.http import HttpResponse
from django.shortcuts import render
from listings.models import Band

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

def hello(request):
    bands = Band.objects.all()
    return render(request, 'listings/hello.html', context={'bands': bands})

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

def contact(request):
    return HttpResponse(test_url)

