# Generated by Django 5.0 on 2024-01-03 04:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dataset', '0023_remove_eventcard_rewers'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('image', models.ImageField(blank=True, null=True, upload_to='dices/')),
            ],
        ),
    ]
