# Generated by Django 5.0 on 2024-01-08 13:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0035_alter_game_demands_token'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='demands_token',
            field=models.JSONField(blank=True, default=['basse-terre', 'bridgetown', 'caracas', 'cartagena', 'curacao', 'nassau', 'havana', 'old-providence', 'petite-goave', 'port-royal', 'san-juan', 'santo-domingo', 'st-john', 'st-maarten', 'trinidad', 'tortuga'], null=True),
        ),
    ]
