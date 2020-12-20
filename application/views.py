from django.shortcuts import render, get_object_or_404
from .models import *

# Create your views here.

def post_list(request):
	empreendimentos = Empreendimento.objects.all()
	casas = Casa.objects.all()
	return render(request, 'index.html', {'empreendimentos': empreendimentos, 'casas': casas})

def empreendimento_detalhes(request, pk):
	imovel = get_object_or_404(Empreendimento, pk=pk)
	unidades = Unidade.objects.filter(empreendimento=imovel).extra(select={'numero': 'CAST(numero AS INTEGER)'}).order_by('numero')
	midias = MidiaEmpreendimento.objects.filter(empreendimento=imovel)
	empreendimentos = Empreendimento.objects.all()
	casas = Casa.objects.all()
	return render(request, 'tabelas.html', {'empreendimentos': empreendimentos, 'casas': casas, 'imovel': imovel, 'unidades': unidades, 'midias': midias})

def casa_detalhes(request, pk):
	imovel = get_object_or_404(Casa, pk=pk)
	empreendimentos = Empreendimento.objects.all()
	midias = MidiaCasa.objects.filter(casa=imovel)
	casas = Casa.objects.all()
	return render(request, 'tabelas_casa.html', {'empreendimentos': empreendimentos, 'casas': casas, 'imovel': imovel, 'midias': midias})
