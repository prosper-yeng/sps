# Generated by Django 4.0.1 on 2022-05-07 12:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('district', '0001_initial'),
        ('constituency', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='constituency',
            name='constituency_district',
        ),
        migrations.AlterField(
            model_name='constituency',
            name='district',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='district', to='district.district'),
        ),
    ]
