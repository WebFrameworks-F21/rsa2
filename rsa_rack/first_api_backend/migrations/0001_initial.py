# Generated by Django 3.2.5 on 2021-12-06 04:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ipv4_network',
            fields=[
                ('name', models.CharField(max_length=200, primary_key=True, serialize=False, unique=True)),
                ('ip_range', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='PatchPanel',
            fields=[
                ('id', models.IntegerField(auto_created=True, primary_key=True, serialize=False)),
                ('size', models.IntegerField()),
                ('number_of_ports', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Rack',
            fields=[
                ('id', models.IntegerField(auto_created=True, primary_key=True, serialize=False)),
                ('size', models.IntegerField()),
                ('location', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Router',
            fields=[
                ('id', models.IntegerField(auto_created=True, primary_key=True, serialize=False)),
                ('size', models.IntegerField()),
                ('rack_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='first_api_backend.rack')),
            ],
        ),
        migrations.CreateModel(
            name='Switch',
            fields=[
                ('id', models.IntegerField(auto_created=True, primary_key=True, serialize=False)),
                ('size', models.IntegerField()),
                ('network_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='first_api_backend.ipv4_network')),
                ('rack_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='first_api_backend.rack')),
                ('router_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='first_api_backend.router')),
            ],
        ),
        migrations.CreateModel(
            name='Server',
            fields=[
                ('id', models.IntegerField(auto_created=True, primary_key=True, serialize=False)),
                ('size', models.IntegerField()),
                ('owner', models.CharField(max_length=200)),
                ('patch_panel_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='first_api_backend.patchpanel')),
                ('rack_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='first_api_backend.rack')),
            ],
        ),
        migrations.AddField(
            model_name='patchpanel',
            name='rack_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='first_api_backend.rack'),
        ),
        migrations.AddField(
            model_name='patchpanel',
            name='switch_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='first_api_backend.switch'),
        ),
        migrations.CreateModel(
            name='NetworkInterfaceCard',
            fields=[
                ('id', models.IntegerField(auto_created=True, primary_key=True, serialize=False)),
                ('ip_address', models.CharField(max_length=1000, unique=True)),
                ('server_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='first_api_backend.server')),
            ],
        ),
        migrations.CreateModel(
            name='BatteryBackup',
            fields=[
                ('id', models.IntegerField(auto_created=True, primary_key=True, serialize=False)),
                ('size', models.IntegerField()),
                ('rack_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='first_api_backend.rack')),
            ],
        ),
    ]
