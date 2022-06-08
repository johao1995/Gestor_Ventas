from django.db import models
from apps.cliente.models import Cliente
from apps.vendedor.models import Vendedor

class Pedido(models.Model):
    cantidad=models.PositiveIntegerField(verbose_name='Cantidad')
    fecha=models.DateField(auto_now=True,verbose_name="Registro")
    cliente=models.ForeignKey(Cliente,on_delete=models.CASCADE,verbose_name='Cliente')
    vendedor=models.ForeignKey(Vendedor,on_delete=models.CASCADE,verbose_name='Vendedor')

    def __str__(self):
        return str(self.cantidad)
    
    class Meta:
        verbose_name_plural='Pedidos'
        db_table='pedido'
        ordering=('id',)
