# Generated by Django 2.0.4 on 2018-06-09 02:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cadd', '0006_auto_20180608_2353'),
    ]

    operations = [
        migrations.AlterField(
            model_name='parametros',
            name='defaultitensporpagina',
            field=models.PositiveSmallIntegerField(choices=[(None, 'Selecione o total de itens por página'), (5, 5), (10, 10), (15, 15), (20, 20), (25, 25), (30, 30), (35, 35), (40, 40), (45, 45), (50, 50)], default=5),
        ),
        migrations.AlterField(
            model_name='parametros',
            name='maxcreditosporperiodopreta',
            field=models.PositiveSmallIntegerField(default=20),
        ),
        migrations.AlterField(
            model_name='parametros',
            name='qtdperiodoslaranja',
            field=models.CharField(default='2 * N', max_length=10),
        ),
        migrations.AlterField(
            model_name='parametros',
            name='qtdperiodosvermelha',
            field=models.CharField(default='4 * N - 3', max_length=10),
        ),
        migrations.AlterField(
            model_name='parametros',
            name='reprovacurso8periodoslaranja',
            field=models.PositiveSmallIntegerField(default=2),
        ),
        migrations.AlterField(
            model_name='parametros',
            name='reprovacurso8periodosvermelha',
            field=models.PositiveSmallIntegerField(default=3),
        ),
        migrations.AlterField(
            model_name='parametros',
            name='reprovademaiscursoslaranja',
            field=models.PositiveSmallIntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='parametros',
            name='reprovademaiscursosvermelha',
            field=models.PositiveSmallIntegerField(default=2),
        ),
    ]