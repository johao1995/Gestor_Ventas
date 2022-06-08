from django.contrib import admin
from .models import Vendedor

class VendedorAdmin(admin.ModelAdmin):
    list_display=(
        'id',
        'first_name',
        'last_name',
        'city',
        'comision'
    )

admin.site.register(Vendedor,VendedorAdmin)