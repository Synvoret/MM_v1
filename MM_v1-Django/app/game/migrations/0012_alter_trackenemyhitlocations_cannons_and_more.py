# Generated by Django 5.0 on 2024-01-04 04:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0011_trackenemyhitlocations'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trackenemyhitlocations',
            name='cannons',
            field=models.IntegerField(default=5),
        ),
        migrations.AlterField(
            model_name='trackenemyhitlocations',
            name='cargo',
            field=models.IntegerField(default=2),
        ),
        migrations.AlterField(
            model_name='trackenemyhitlocations',
            name='crew',
            field=models.IntegerField(default=4),
        ),
        migrations.AlterField(
            model_name='trackenemyhitlocations',
            name='game_number',
            field=models.ImageField(default=100, upload_to=''),
        ),
        migrations.AlterField(
            model_name='trackenemyhitlocations',
            name='masts',
            field=models.IntegerField(default=3),
        ),
    ]
