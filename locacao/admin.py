from django.contrib import admin
from locacao.models import Phone, Renter, Room, Tenancy


@admin.site.register(Tenancy)
class TenancyAdmin (admin.ModelAdmin):

    fields = (
        ('street', 'number', ),
    )


@admin.site.register(Room)
class RoomAdmin (admin.ModelAdmin):

    fields = (
        ('tenancy', 'number', ),
        ('gender', 'capacity', ),
    )


@admin.site.register(Renter)
class RenterAdmin (admin.ModelAdmin):

    fields = (
        'full_name',
        'responsible',
        ('cpf', 'rg', 'birthday', ),
        ('address', 'neighborhood', 'cep', ),
        ('city', 'state', 'country', ),
        'room',
        'phones',
    )


@admin.site.register(Phone)
class PhoneAdmin (admin.ModelAdmin):

    fields = (
        'type',
        ('ddi', 'ddd', 'number', ),
    )
