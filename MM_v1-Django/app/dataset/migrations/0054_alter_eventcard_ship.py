# Generated by Django 5.0 on 2024-01-10 07:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dataset', '0053_alter_eventcard_card'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eventcard',
            name='ship',
            field=models.CharField(blank=True, choices=[('Brig', 'Brig'), ('Flute', 'Flute'), ('Frigate', 'Frigate'), ('Galleon', 'Galleon'), ('Man-o-War', 'Man-o-War'), ('Sloop', 'Sloop')], max_length=50, null=True),
        ),
    ]