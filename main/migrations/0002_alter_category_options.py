# Generated by Django 4.2.5 on 2023-10-08 21:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ('product_name',), 'verbose_name': 'Категория', 'verbose_name_plural': 'Категории'},
        ),
    ]
