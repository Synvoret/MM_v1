# Generated by Django 5.0 on 2024-01-10 04:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dataset', '0050_alter_eventcard_ship'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ship',
            name='colour',
            field=models.CharField(blank=True, choices=[('Black', 'Black'), ('Blue', 'Blue'), ('Green', 'Green'), ('Large Pirate', 'Large Pirate'), ('Red', 'Red'), ('Small Pirate', 'Small Pirate'), ('Yellow', 'Yellow'), ('Treasure', 'Treasure')], max_length=50, null=True),
        ),
    ]
