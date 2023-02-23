# Generated by Django 4.1.6 on 2023-02-23 18:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('endpoints', '0002_rename_username_restaurant_usuario_plato_restaurante_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='CategoriasporRestaurante',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='endpoints.categoria_plato')),
                ('restaurant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='endpoints.restaurant')),
            ],
        ),
    ]
