# Generated by Django 5.0 on 2024-03-22 05:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dataset', '0078_alter_captaincard_home_port_alter_missioncard_port'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('image', models.ImageField(blank=True, null=True, upload_to='boardTiles/')),
            ],
        ),
    ]
