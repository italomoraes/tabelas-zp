# Generated by Django 3.1.4 on 2020-12-20 21:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0005_auto_20201220_1753'),
    ]

    operations = [
        migrations.AlterField(
            model_name='unidade',
            name='boxe',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='unidade',
            name='restante_da_entrada',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=20, null=True),
        ),
        migrations.AlterField(
            model_name='unidade',
            name='sinal_na_assinatura_do_contrato',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=20, null=True),
        ),
        migrations.AlterField(
            model_name='unidade',
            name='valor',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=20, null=True),
        ),
    ]
