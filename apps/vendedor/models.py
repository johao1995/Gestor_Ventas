from django.db import models


class Vendedor(models.Model):
    city_choices=(
        ('Montevideo','Montevideo'),
        ('Brazilia','Brazilia')
    )

    first_name=models.CharField(max_length=50,verbose_name='Nombre')
    last_name=models.CharField(max_length=50,verbose_name='Apellido')
    city=models.CharField(max_length=40,choices=city_choices,verbose_name='CIudad')
    comision=models.DecimalField(default=0.00,max_digits=9,decimal_places=2,verbose_name='Comision')
    image=models.ImageField(upload_to='vendedor/img',null=True,blank=True,verbose_name='Foto')

    def __str__(self):
        return self.first_name
    
    class Meta:
        verbose_name_plural='Vendedores'
        db_table='vendedor'
        ordering=('id',)