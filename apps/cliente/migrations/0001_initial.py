# Generated by Django 4.0.5 on 2022-06-08 17:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50, verbose_name='Nombre')),
                ('last_name', models.CharField(max_length=50, verbose_name='Apellido')),
                ('city', models.CharField(choices=[('Lima', 'Lima'), ('Arequipa', 'Arequipa'), ('Trujillo', 'Trujillo')], max_length=20, verbose_name='CIudad')),
                ('category', models.CharField(choices=[('Normal', 'Normal'), ('Premiun', 'Premium')], max_length=50, verbose_name='Categoria')),
                ('fecha', models.DateField(auto_now=True, verbose_name='Atencion')),
                ('image', models.ImageField(blank=True, null=True, upload_to='cliente/img', verbose_name='Foto')),
            ],
            options={
                'verbose_name_plural': 'CLientes',
                'db_table': 'cliente',
                'ordering': ('id',),
            },
        ),
    ]
