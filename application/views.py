from django.shortcuts import render

# Create your views here.

def post_list(request):
    return render(request, 'index.html', {})

def empreendimento_detalhes(request):
    return render(request, 'tabelas.html', {})

def casa_detalhes(request):
    return render(request, 'tabelas.html', {})