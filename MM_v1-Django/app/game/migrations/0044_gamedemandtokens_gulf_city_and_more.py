# Generated by Django 5.0 on 2024-01-09 10:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0043_gameshipmodifications'),
    ]

    operations = [
        migrations.AddField(
            model_name='gamedemandtokens',
            name='gulf_city',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='gameshipmodifications',
            name='gulf_city',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
