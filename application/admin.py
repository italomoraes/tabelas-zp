from django.contrib import admin
from application.models import *

admin.site.site_header = 'Painel do corretor'

# Register your models here.
admin.site.register(Empreendimento)
admin.site.register(Unidade)
admin.site.register(MidiaEmpreendimento)
admin.site.register(Casa)
admin.site.register(MidiaCasa)

