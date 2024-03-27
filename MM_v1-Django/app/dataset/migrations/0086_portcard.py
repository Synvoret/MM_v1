# Generated by Django 5.0 on 2024-03-27 05:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dataset', '0085_alter_commandboatcard_awers_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='PortCard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='ports/')),
                ('sea_zone', models.CharField(blank=True, choices=[('Basse-Terre', 'Basse-Terre'), ('Bridgetown', 'Bridgetown'), ('Caracas', 'Caracas'), ('Cartagena', 'Cartagena'), ('Curacao', 'Curacao'), ('Gulf City', 'Gulf City'), ('Havana', 'Havana'), ('Nassau', 'Nassau'), ('Old Providence', 'Old Providence'), ('Petite Goave', 'Petite Goave'), ('Port Royal', 'Port Royal'), ('San Juan', 'San Juan'), ('Santo Domingo', 'Santo Domingo'), ('St John', 'St John'), ('St Maarten', 'St Maarten'), ('The Caribbean Sea', 'The Caribbean Sea'), ('Tortuga', 'Tortuga'), ('Trinidad', 'Trinidad')], max_length=50, null=True)),
                ('nationality', models.CharField(blank=True, choices=[('Dutch', 'Dutch'), ('French', 'French'), ('English', 'English'), ('Spanish', 'Spanish')], max_length=50, null=True)),
                ('fortitude', models.IntegerField(blank=True, null=True)),
                ('stockpile', models.IntegerField(blank=True, null=True)),
                ('soldiers', models.IntegerField(blank=True, null=True)),
                ('cannons', models.IntegerField(blank=True, null=True)),
                ('defensibility', models.IntegerField(blank=True, null=True)),
                ('boats', models.IntegerField(blank=True, null=True)),
            ],
        ),
    ]