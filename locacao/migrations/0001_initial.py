# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-25 22:34
from __future__ import unicode_literals

from django.conf import settings
import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0008_alter_user_username_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Phone',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='criado em')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='atualizado pela última vez em')),
                ('is_active', models.BooleanField(default=True, verbose_name='está ativo')),
                ('type', models.BooleanField(choices=[(True, 'Celular'), (False, 'Telefone fixo')], verbose_name='tipo de telefone')),
                ('ddi', models.SmallIntegerField(default=55, verbose_name='DDI')),
                ('ddd', models.SmallIntegerField(default=21, verbose_name='DDD')),
                ('number', models.CharField(max_length=10, verbose_name='número')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Renter',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('full_name', models.CharField(max_length=150, verbose_name='nome completo')),
                ('responsible', models.CharField(max_length=150, verbose_name='responsável (se menor de 18)')),
                ('cpf', models.CharField(max_length=15, verbose_name='CPF')),
                ('rg', models.CharField(max_length=15, verbose_name='RG')),
                ('birthday', models.DateField(verbose_name='data de nascimento')),
                ('address', models.CharField(max_length=200, verbose_name='endereço')),
                ('neighborhood', models.CharField(max_length=50, verbose_name='bairro')),
                ('city', models.CharField(max_length=50, verbose_name='cidade')),
                ('state', models.CharField(max_length=50, verbose_name='estado')),
                ('country', models.CharField(max_length=50, verbose_name='país')),
                ('cep', models.CharField(max_length=8, verbose_name='CEP')),
            ],
            options={
                'abstract': False,
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
            },
            bases=('auth.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='criado em')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='atualizado pela última vez em')),
                ('is_active', models.BooleanField(default=True, verbose_name='está ativo')),
                ('name', models.CharField(default='Não definido', max_length=120, verbose_name='nome')),
                ('number', models.PositiveSmallIntegerField(verbose_name='nº')),
                ('gender', models.NullBooleanField(choices=[(True, 'Masculino'), (False, 'Feminino'), (None, 'Misto')], default=None, verbose_name='sexo')),
                ('capacity', models.SmallIntegerField(verbose_name='capacidade')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Tenancy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='criado em')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='atualizado pela última vez em')),
                ('is_active', models.BooleanField(default=True, verbose_name='está ativo')),
                ('street', models.CharField(max_length=100, verbose_name='rua')),
                ('number', models.IntegerField(verbose_name='nº')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='room',
            name='tenancy',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rooms', to='locacao.Tenancy'),
        ),
        migrations.AddField(
            model_name='renter',
            name='room',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='users', to='locacao.Room', verbose_name='quarto'),
        ),
        migrations.AddField(
            model_name='phone',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='phones', to='locacao.Renter', verbose_name='dono'),
        ),
    ]