# Generated by Django 3.0.12 on 2021-11-19 09:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_category_cciidd'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='producttranslation',
            name='slug',
        ),
    ]
