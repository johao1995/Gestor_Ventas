# Generated by Django 4.0.5 on 2022-06-08 17:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Vendedor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50, verbose_name='Nombre')),
                ('last_name', models.CharField(max_length=50, verbose_name='Apellido')),
                ('city', models.CharField(choices=[('Montevideo', 'Montevideo'), ('Brazilia', 'Brazilia')], max_length=40, verbose_name='CIudad')),
                ('comision', models.DecimalField(decimal_places=2, default=0.0, max_digits=9, verbose_name='Comision')),
                ('image', models.ImageField(blank=True, null=True, upload_to='vendedor/img', verbose_name='Foto')),
            ],
            options={
                'verbose_name_plural': 'Vendedores',
                'db_table': 'vendedor',
                'ordering': ('id',),
            },
        ),
    ]
