# Generated by Django 5.0 on 2024-01-04 05:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dataset', '0027_remove_missioncard_rewers_alter_missioncard_card'),
    ]

    operations = [
        migrations.AddField(
            model_name='missioncard',
            name='notess',
            field=models.TextField(blank=True, max_length=1000, null=True),
        ),
    ]
