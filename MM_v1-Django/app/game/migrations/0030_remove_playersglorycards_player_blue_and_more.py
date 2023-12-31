# Generated by Django 5.0 on 2024-01-06 18:11

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dataset', '0045_remove_glorycard_rewers_alter_glorycard_notes'),
        ('game', '0029_playersglorycards'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='playersglorycards',
            name='player_blue',
        ),
        migrations.RemoveField(
            model_name='playersglorycards',
            name='player_green',
        ),
        migrations.RemoveField(
            model_name='playersglorycards',
            name='player_red',
        ),
        migrations.RemoveField(
            model_name='playersglorycards',
            name='player_yellow',
        ),
        migrations.AddField(
            model_name='playersglorycards',
            name='glory_card_1',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='glory_card_1', to='dataset.glorycard'),
        ),
        migrations.AddField(
            model_name='playersglorycards',
            name='glory_card_2',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='glory_card_2', to='dataset.glorycard'),
        ),
        migrations.AddField(
            model_name='playersglorycards',
            name='glory_card_3',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='glory_card_3', to='dataset.glorycard'),
        ),
        migrations.AddField(
            model_name='playersglorycards',
            name='glory_card_4',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='glory_card_4', to='dataset.glorycard'),
        ),
        migrations.AddField(
            model_name='playersglorycards',
            name='glory_card_5',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='glory_card_5', to='dataset.glorycard'),
        ),
        migrations.AddField(
            model_name='playersglorycards',
            name='glory_card_6',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='glory_card_6', to='dataset.glorycard'),
        ),
        migrations.AddField(
            model_name='playersglorycards',
            name='player_colour',
            field=models.CharField(blank=True, choices=[('Blue', 'Blue'), ('Green', 'Green'), ('Red', 'Red'), ('Yellow', 'Yellow')], max_length=20, null=True),
        ),
    ]
