# Generated by Django 5.0 on 2024-01-20 01:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0013_alter_seazone_e_direction_alter_seazone_n_direction_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='seazone',
            name='feature_text',
            field=models.TextField(blank=True, max_length=2000, null=True),
        ),
    ]