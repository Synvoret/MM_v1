# Generated by Django 5.0 on 2023-12-21 05:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0003_board_board'),
    ]

    operations = [
        migrations.AddField(
            model_name='board',
            name='name',
            field=models.CharField(default='Board Game', max_length=150),
        ),
    ]
