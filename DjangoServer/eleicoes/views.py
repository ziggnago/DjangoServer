from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'index.html', {'name': 'bolsonaro'})

def add(request):

    valor_1 = int(request.GET['num1'])
    valor_2 = int(request.GET['num2'])

    resultado = valor_1 + valor_2

    return render(request, 'index.html', {'resultado': resultado, 'valor_1': valor_1, 'valor_2': valor_2})