# Generated by Django 3.0.12 on 2021-11-19 09:42

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_remove_producttranslation_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='categorytranslation',
            name='slug',
        ),
        migrations.AddField(
            model_name='category',
            name='slug',
            field=models.SlugField(default=django.utils.timezone.now, max_length=200, unique=True),
            preserve_default=False,
        ),
    ]