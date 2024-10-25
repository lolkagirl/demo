from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index (request):
    context = {
        'title': 'Главная',
        
    }

    return render(request, 'main/index.html', context)

def contact (request):
    context = {
        'title': 'Контакты',
        
    }

    return render(request, 'main/contact.html', context)