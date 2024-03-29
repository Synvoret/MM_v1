# Generated by Django 5.0 on 2024-01-11 22:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0012_seazone_e_direction_seazone_n_direction_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='seazone',
            name='e_direction',
            field=models.CharField(blank=True, choices=[('Basse-Terre', 'Basse-Terre'), ('Bridgetown', 'Bridgetown'), ('Caracas', 'Caracas'), ('Cartagena', 'Cartagena'), ('Curacao', 'Curacao'), ('Gulf City', 'Gulf City'), ('Havana', 'Havana'), ('Nassau', 'Nassau'), ('Old Providence', 'Old Providence'), ('Petite Goave', 'Petite Goave'), ('Port Royal', 'Port Royal'), ('San Juan', 'San Juan'), ('Santo Domingo', 'Santo Domingo'), ('St John', 'St John'), ('St Maarten', 'St Maarten'), ('The Carribean Sea', 'The Carribean Sea'), ('Tortuga', 'Tortuga'), ('Trinidad', 'Trinidad')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='seazone',
            name='n_direction',
            field=models.CharField(blank=True, choices=[('Basse-Terre', 'Basse-Terre'), ('Bridgetown', 'Bridgetown'), ('Caracas', 'Caracas'), ('Cartagena', 'Cartagena'), ('Curacao', 'Curacao'), ('Gulf City', 'Gulf City'), ('Havana', 'Havana'), ('Nassau', 'Nassau'), ('Old Providence', 'Old Providence'), ('Petite Goave', 'Petite Goave'), ('Port Royal', 'Port Royal'), ('San Juan', 'San Juan'), ('Santo Domingo', 'Santo Domingo'), ('St John', 'St John'), ('St Maarten', 'St Maarten'), ('The Carribean Sea', 'The Carribean Sea'), ('Tortuga', 'Tortuga'), ('Trinidad', 'Trinidad')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='seazone',
            name='ne_direction',
            field=models.CharField(blank=True, choices=[('Basse-Terre', 'Basse-Terre'), ('Bridgetown', 'Bridgetown'), ('Caracas', 'Caracas'), ('Cartagena', 'Cartagena'), ('Curacao', 'Curacao'), ('Gulf City', 'Gulf City'), ('Havana', 'Havana'), ('Nassau', 'Nassau'), ('Old Providence', 'Old Providence'), ('Petite Goave', 'Petite Goave'), ('Port Royal', 'Port Royal'), ('San Juan', 'San Juan'), ('Santo Domingo', 'Santo Domingo'), ('St John', 'St John'), ('St Maarten', 'St Maarten'), ('The Carribean Sea', 'The Carribean Sea'), ('Tortuga', 'Tortuga'), ('Trinidad', 'Trinidad')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='seazone',
            name='nw_direction',
            field=models.CharField(blank=True, choices=[('Basse-Terre', 'Basse-Terre'), ('Bridgetown', 'Bridgetown'), ('Caracas', 'Caracas'), ('Cartagena', 'Cartagena'), ('Curacao', 'Curacao'), ('Gulf City', 'Gulf City'), ('Havana', 'Havana'), ('Nassau', 'Nassau'), ('Old Providence', 'Old Providence'), ('Petite Goave', 'Petite Goave'), ('Port Royal', 'Port Royal'), ('San Juan', 'San Juan'), ('Santo Domingo', 'Santo Domingo'), ('St John', 'St John'), ('St Maarten', 'St Maarten'), ('The Carribean Sea', 'The Carribean Sea'), ('Tortuga', 'Tortuga'), ('Trinidad', 'Trinidad')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='seazone',
            name='s_direction',
            field=models.CharField(blank=True, choices=[('Basse-Terre', 'Basse-Terre'), ('Bridgetown', 'Bridgetown'), ('Caracas', 'Caracas'), ('Cartagena', 'Cartagena'), ('Curacao', 'Curacao'), ('Gulf City', 'Gulf City'), ('Havana', 'Havana'), ('Nassau', 'Nassau'), ('Old Providence', 'Old Providence'), ('Petite Goave', 'Petite Goave'), ('Port Royal', 'Port Royal'), ('San Juan', 'San Juan'), ('Santo Domingo', 'Santo Domingo'), ('St John', 'St John'), ('St Maarten', 'St Maarten'), ('The Carribean Sea', 'The Carribean Sea'), ('Tortuga', 'Tortuga'), ('Trinidad', 'Trinidad')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='seazone',
            name='se_direction',
            field=models.CharField(blank=True, choices=[('Basse-Terre', 'Basse-Terre'), ('Bridgetown', 'Bridgetown'), ('Caracas', 'Caracas'), ('Cartagena', 'Cartagena'), ('Curacao', 'Curacao'), ('Gulf City', 'Gulf City'), ('Havana', 'Havana'), ('Nassau', 'Nassau'), ('Old Providence', 'Old Providence'), ('Petite Goave', 'Petite Goave'), ('Port Royal', 'Port Royal'), ('San Juan', 'San Juan'), ('Santo Domingo', 'Santo Domingo'), ('St John', 'St John'), ('St Maarten', 'St Maarten'), ('The Carribean Sea', 'The Carribean Sea'), ('Tortuga', 'Tortuga'), ('Trinidad', 'Trinidad')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='seazone',
            name='sw_direction',
            field=models.CharField(blank=True, choices=[('Basse-Terre', 'Basse-Terre'), ('Bridgetown', 'Bridgetown'), ('Caracas', 'Caracas'), ('Cartagena', 'Cartagena'), ('Curacao', 'Curacao'), ('Gulf City', 'Gulf City'), ('Havana', 'Havana'), ('Nassau', 'Nassau'), ('Old Providence', 'Old Providence'), ('Petite Goave', 'Petite Goave'), ('Port Royal', 'Port Royal'), ('San Juan', 'San Juan'), ('Santo Domingo', 'Santo Domingo'), ('St John', 'St John'), ('St Maarten', 'St Maarten'), ('The Carribean Sea', 'The Carribean Sea'), ('Tortuga', 'Tortuga'), ('Trinidad', 'Trinidad')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='seazone',
            name='w_direction',
            field=models.CharField(blank=True, choices=[('Basse-Terre', 'Basse-Terre'), ('Bridgetown', 'Bridgetown'), ('Caracas', 'Caracas'), ('Cartagena', 'Cartagena'), ('Curacao', 'Curacao'), ('Gulf City', 'Gulf City'), ('Havana', 'Havana'), ('Nassau', 'Nassau'), ('Old Providence', 'Old Providence'), ('Petite Goave', 'Petite Goave'), ('Port Royal', 'Port Royal'), ('San Juan', 'San Juan'), ('Santo Domingo', 'Santo Domingo'), ('St John', 'St John'), ('St Maarten', 'St Maarten'), ('The Carribean Sea', 'The Carribean Sea'), ('Tortuga', 'Tortuga'), ('Trinidad', 'Trinidad')], max_length=50, null=True),
        ),
    ]
