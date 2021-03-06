# Generated by Django 3.2.5 on 2021-12-08 03:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('first_api_backend', '0005_auto_20211207_2230'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ipv4_network',
            name='ip_address',
            field=models.CharField(max_length=1000, unique=True),
        ),
        migrations.AlterField(
            model_name='networkinterfacecard',
            name='ip_address',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='first_api_backend.ipv4_network', to_field='ip_address'),
        ),
    ]
