from django.shortcuts import render


def index(request):
    return render(request, 'site/index.html')


def contact(request):
    return render(request, 'site/contact.html')


def about(request):
    return render(request, 'site/about.html')


def faqs(request):
    return render(request, 'site/faqs.html')