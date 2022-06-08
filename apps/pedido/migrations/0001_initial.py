# Generated by Django 4.0.5 on 2022-06-08 17:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('vendedor', '0001_initial'),
        ('cliente', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pedido',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.PositiveIntegerField(verbose_name='Cantidad')),
                ('fecha', models.DateField(auto_now=True, verbose_name='Registro')),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cliente.cliente', verbose_name='Cliente')),
                ('vendedor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vendedor.vendedor', verbose_name='Vendedor')),
            ],
            options={
                'verbose_name_plural': 'Pedidos',
                'db_table': 'pedido',
                'ordering': ('id',),
            },
        ),
    ]