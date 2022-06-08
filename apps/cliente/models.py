from django.db import models

class Cliente(models.Model):
    city_choices=(
        ('Lima','Lima'),
        ('Arequipa','Arequipa'),
        ('Trujillo','Trujillo')
    )
    category_choices=(
        ('Normal','Normal'),
        ('Premiun','Premium')
    )
    first_name=models.CharField(max_length=50,verbose_name='Nombre')
    last_name=models.CharField(max_length=50,verbose_name='Apellido')
    city=models.CharField(max_length=20,choices=city_choices,verbose_name='CIudad')
    category=models.CharField(max_length=50,choices=category_choices,verbose_name='Categoria')
    fecha=models.DateField(auto_now=True,verbose_name="Atencion")
    image=models.ImageField(upload_to='cliente/img',null=True,blank=True,verbose_name='Foto')

    def __str__(self):
        return self.first_name
    
    class Meta:
        verbose_name_plural='CLientes'
        db_table='cliente'
        ordering=('id',)