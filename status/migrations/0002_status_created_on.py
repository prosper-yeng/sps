# Generated by Django 4.0.1 on 2022-05-22 12:39

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('status', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='status',
            name='created_on',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
