# Generated by Django 4.0.1 on 2022-05-07 12:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='SelectItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=100)),
                ('value', models.CharField(max_length=100)),
                ('text', models.CharField(max_length=100)),
                ('parent', models.CharField(max_length=100, null=True)),
                ('parent_name', models.CharField(max_length=250, null=True)),
                ('secured', models.BooleanField(default=True)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('modified_on', models.DateTimeField(auto_now=True)),
                ('status', models.CharField(choices=[('created', 'Created'), ('approved', 'Approved'), ('active', 'Active'), ('deactivate', 'Deactivate'), ('delete', 'Delete'), ('closed', 'Closed')], default='active', max_length=100)),
                ('created_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('type',),
            },
        ),
    ]
