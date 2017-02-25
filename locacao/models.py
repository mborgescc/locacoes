# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User
from util.models import BaseModel


class Phone (BaseModel):

    MOBILE = True
    LANDLINE = False

    TYPE_CHOICES = (
        (MOBILE, "Celular"),
        (LANDLINE, "Telefone fixo"),
    )

    type = models.BooleanField(
        choices=TYPE_CHOICES,
        verbose_name="tipo de telefone"
    )

    ddi = models.SmallIntegerField(
        verbose_name="DDI",
        default=55
    )

    ddd = models.SmallIntegerField(
        verbose_name="DDD",
        default=21
    )

    number = models.CharField(
        verbose_name="número",
        max_length=10
    )

    owner = models.ForeignKey(
        "Renter",
        verbose_name="dono",
        related_name="phones"
    )

    def __unicode__(self):
        return "+{} {} {}-{}".format(
            self.owner,
            self.ddi,
            self.ddd,
            self.number[:-4],
            self.number[-4:]
        )


class Renter (User):

    full_name = models.CharField(
        verbose_name="nome completo",
        max_length=150
    )

    responsible = models.CharField(
        verbose_name="responsável (se menor de 18)",
        max_length=150
    )

    room = models.ForeignKey(
        to="Room",
        verbose_name="quarto",
        related_name="users"
    )

    cpf = models.CharField(
        verbose_name="CPF",
        max_length=15,
    )

    rg = models.CharField(
        verbose_name="RG",
        max_length=15
    )

    birthday = models.DateField(
        verbose_name="data de nascimento"
    )

    address = models.CharField(
        verbose_name="endereço",
        max_length=200
    )

    neighborhood = models.CharField(
        verbose_name="bairro",
        max_length=50
    )

    city = models.CharField(
        verbose_name="cidade",
        max_length=50
    )

    state = models.CharField(
        verbose_name="estado",
        max_length=50
    )

    country = models.CharField(
        verbose_name="país",
        max_length=50
    )

    cep = models.CharField(
        verbose_name="CEP",
        max_length=8
    )

    def __unicode__(self):
        return "{}".format(self.full_name)


class Tenancy (BaseModel):

    MALE = "Masculino"
    FEMALE = "Feminino"
    MIXED = "Misto"

    street = models.CharField(
        verbose_name="rua",
        max_length=100,
    )

    number = models.IntegerField(
        verbose_name="nº"
    )

    def __unicode__(self):
        return "{} {}".format(
            self.street,
            self.number
        )

    @property
    def gender(self):
        if not Room.objects.filter(
                tenancy=self,
                gender=Room.MALE
        ):
            return self.FEMALE
        elif not Room.objects.filter(
                tenancy=self,
                gender=Room.FEMALE
        ):
            return self.MALE
        else:
            return self.MIXED


class Room (BaseModel):

    MALE = True
    FEMALE = False

    GENDER_CHOICES = (
        (MALE, "Masculino"),
        (FEMALE, "Feminino"),
    )

    name = models.CharField(
        verbose_name="nome",
        max_length=120,
        default="Não definido",
    )

    number = models.PositiveSmallIntegerField(
        verbose_name="nº",
    )

    gender = models.BooleanField(
        choices=GENDER_CHOICES,
        verbose_name="sexo",
        default=MALE
    )

    capacity = models.SmallIntegerField(
        verbose_name="capacidade",
    )

    tenancy = models.ForeignKey(
        to="Tenancy",
        on_delete=models.CASCADE,
        related_name="rooms"
    )

    def __unicode__(self):
        return "{}".format(self.name)

    def build_name(self):
        self.name = "{} {} - Quarto {}".format(
            self.tenancy.street,
            self.tenancy.number,
            self.number
        )
        self.save()



