# Generated by Django 5.0.6 on 2024-05-25 22:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MainApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='description',
            field=models.TextField(default='Базовое описание', max_length=1000),
        ),
    ]
