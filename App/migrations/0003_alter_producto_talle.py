# Generated by Django 4.2 on 2024-12-09 17:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0002_categoria_producto_subcategoria_delete_curso_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='talle',
            field=models.CharField(max_length=5),
        ),
    ]
