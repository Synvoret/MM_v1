# Generated by Django 5.0 on 2024-01-05 20:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dataset', '0034_specialweapon'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ship',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('image', models.ImageField(blank=True, null=True, upload_to='ships/')),
            ],
        ),
    ]
