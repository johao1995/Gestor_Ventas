from django.contrib import admin
from .models import Pedido

class PedidoAdmin(admin.ModelAdmin):
    list_display=(
        'id',
        'cantidad',
        'fecha',
        'cliente',
        'vendedor'
    )
admin.site.register(Pedido,PedidoAdmin)
