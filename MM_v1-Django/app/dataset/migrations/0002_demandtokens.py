# Generated by Django 5.0 on 2023-12-21 08:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dataset', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DemandTokens',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cargo', models.CharField(max_length=20)),
                ('awers', models.ImageField(blank=True, null=True, upload_to='demandTokens/')),
            ],
        ),
    ]
