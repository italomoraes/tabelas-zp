from django.shortcuts import render
from application.models import *

# Create your views here.

def post_list(request):
	empreendimentos = Empreendimentos.objects.all()
	casas = Casa.objects.all()
	return render(request, 'index.html', {'empreendimentos': empreendimentos, 'casas': casas})

def empreendimento_detalhes(request):
    return render(request, 'tabelas.html', {})

def casa_detalhes(request):
    return render(request, 'tabelas.html', {})