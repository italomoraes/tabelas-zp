from django.db import models

SITUACAO_VAGA = [
	(1, 'Coberta(s)'),
	(2, 'Descoberta(s)'),
	(3, 'Coberta(s) e descoberta(s)')
]

TIPO_MEDIA = [
	(1, 'Link'),
	(2, 'Foto'),
	(3, 'Video'),
	(4, 'Arquivo')
]

ESTAGIO_CASA = [
	(1, 'Em Definição'),
	(2, 'Em Construção'),
	(3, 'Pronta')
]

# Create your models here.
class Empreendimento(models.Model):

	nome = models.CharField(max_length=200)
	endereco = models.CharField(max_length=400)
	icone = models.ImageField(upload_to='empreendimentos/icones/')
	entrega = models.DateField(auto_now=False)
	comentarios = models.TextField(null=True, blank=True)

	def __str__(self):
		return self.nome


class Unidade(models.Model):

	numero = models.CharField(max_length=100)
	metragem = models.IntegerField()
	vaga = models.CharField(max_length=100, null=True, blank=True)
	tipo_de_vaga = models.IntegerField(
		choices = SITUACAO_VAGA
	, null=True, blank=True)
	sinal_na_assinatura_do_contrato = models.DecimalField(max_digits=20, decimal_places=2, null=True, blank=True)
	restante_da_entrada = models.DecimalField(max_digits=20, decimal_places=2, null=True, blank=True)
	boxe = models.CharField(max_length=100, null=True, blank=True)
	valor = models.DecimalField(max_digits=20, decimal_places=2, null=True, blank=True)
	valor_promocional = models.DecimalField(max_digits=20, decimal_places=2, null=True, blank=True)
	vendida = models.BooleanField(default=False)
	empreendimento = models.ForeignKey(Empreendimento, on_delete=models.CASCADE)

	def __str__(self):
		return self.empreendimento.nome + ' - ' + self.numero


class MidiaEmpreendimento(models.Model):

	empreendimento = models.ForeignKey(Empreendimento, on_delete=models.CASCADE)
	nome = models.CharField(max_length=100)
	tipo = models.IntegerField(
		choices = TIPO_MEDIA
	)
	link = models.URLField(max_length=1000, null=True, blank=True)
	arquivo = models.FileField(upload_to='empreendimentos/arquivos/', null=True, blank=True)



class Casa(models.Model):

	nome = models.CharField(max_length=200)
	estagio_da_obra = models.IntegerField(
		choices = ESTAGIO_CASA
	)
	icone = models.ImageField(upload_to='casas/icones/')
	entrega = models.DateField(auto_now=False)
	metragem_do_terreno = models.DecimalField(max_digits=20, decimal_places=2)
	metragem_da_casa = models.DecimalField(max_digits=20, decimal_places=2)
	condominio = models.CharField(max_length=200)
	endereco = models.CharField(max_length=400)
	valor = models.DecimalField(max_digits=20, decimal_places=2)
	comentarios = models.TextField(null=True, blank=True)

	def __str__(self):
		return self.nome


class MidiaCasa(models.Model):

	nome = models.CharField(max_length=200)
	casa = models.ForeignKey(Casa, on_delete=models.CASCADE)
	tipo = models.IntegerField(
		choices = TIPO_MEDIA
	)
	link = models.URLField(max_length=1000, null=True, blank=True)
	arquivo = models.FileField(upload_to='casas/arquivos/', null=True, blank=True)


