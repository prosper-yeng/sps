# Generated by Django 4.0.1 on 2022-05-22 12:39

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('status', '0002_status_created_on'),
        ('district', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='district',
            name='created_on',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='district',
            name='status',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='district_status', to='status.status'),
        ),
    ]
