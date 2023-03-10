# Generated by Django 4.1.6 on 2023-03-01 23:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria_Plato',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('username', models.CharField(max_length=25, primary_key=True, serialize=False)),
                ('password', models.CharField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='Restaurant_Cat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Restaurant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('usuario', models.CharField(max_length=25)),
                ('password', models.CharField(max_length=25)),
                ('nombre', models.CharField(max_length=25)),
                ('descripcion', models.CharField(max_length=500)),
                ('logo', models.CharField(max_length=100)),
                ('estado', models.CharField(choices=[('A', 'activo'), ('I', 'inactivo')], max_length=1)),
                ('categoria_Rest', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='endpoints.restaurant_cat')),
            ],
        ),
        migrations.CreateModel(
            name='Plato',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('precio', models.DecimalField(decimal_places=2, max_digits=4)),
                ('img', models.URLField()),
                ('dscr', models.CharField(max_length=100)),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='endpoints.categoria_plato')),
                ('restaurante', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='endpoints.restaurant')),
            ],
        ),
        migrations.CreateModel(
            name='orden',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('monto', models.DecimalField(decimal_places=2, max_digits=5)),
                ('direccion', models.CharField(max_length=40)),
                ('fecha', models.CharField(max_length=10)),
                ('estado', models.CharField(max_length=10)),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='endpoints.cliente')),
            ],
        ),
        migrations.CreateModel(
            name='Form',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rest', models.CharField(max_length=100)),
                ('valoracion', models.CharField(max_length=2)),
                ('comentario', models.CharField(max_length=250)),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='endpoints.cliente')),
            ],
        ),
        migrations.CreateModel(
            name='CategoriasporRestaurante',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='endpoints.categoria_plato')),
                ('restaurant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='endpoints.restaurant')),
            ],
        ),
    ]
