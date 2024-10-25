from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index (request):
    context = {
        'title': 'Главная',
        'content': ['Aроматы', 'Ручной работы'],
        'words':['Выберите аромат'],
    }

    return render(request, 'main/index.html', context)



def contact(request):
    context = {
        'title': 'Контакты',
        'content': ['Контактные данные'],
        'words':['ПОЗВОНИТЕ НАМ','НАПИШИТЕ НАМ','НАЙДИТЕ НАС',],
    }

    return render(request, 'main/contact.html', context)