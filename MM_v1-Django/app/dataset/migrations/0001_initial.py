# Generated by Django 5.0 on 2023-12-19 18:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CaptainsDeck',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('card', models.CharField(max_length=50, unique=True)),
                ('awers', models.ImageField(blank=True, null=True, upload_to='')),
                ('expansion', models.CharField(blank=True, choices=[('Seas of Glory', 'Seas of Glory'), ('Colors of War', 'Colors of War')], max_length=150, null=True)),
                ('notes', models.CharField(blank=True, max_length=150, null=True)),
                ('rewers', models.ImageField(blank=True, null=True, upload_to='')),
                ('home_port', models.CharField(choices=[('Basse-Terre', 'Basse-Terre'), ('Bridgetown', 'Bridgetown'), ('Caracas', 'Caracas'), ('Cartagena', 'Cartagena'), ('Curacao', 'Curacao'), ('Havana', 'Havana'), ('Nassau', 'Nassau'), ('Old Providence', 'Old Providence'), ('Petite Goave', 'Petite Goave'), ('Port Royal', 'Port Royal'), ('San Juan', 'San Juan'), ('Santo Domingo', 'Santo Domingo'), ('St. John', 'St. John'), ('St. Maarten', 'St. Maarten'), ('Tortuga', 'Tortuga'), ('Trinidad', 'Trinidad')], max_length=30)),
                ('nationality', models.CharField(choices=[('DU', 'Dutch'), ('FR', 'French'), ('EN', 'English'), ('SP', 'Spanich')], max_length=30)),
                ('seamanship', models.IntegerField()),
                ('scouting', models.IntegerField()),
                ('leadership', models.IntegerField()),
                ('influence', models.IntegerField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='EventsDeck',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('card', models.CharField(max_length=50, unique=True)),
                ('awers', models.ImageField(blank=True, null=True, upload_to='')),
                ('expansion', models.CharField(blank=True, choices=[('Seas of Glory', 'Seas of Glory'), ('Colors of War', 'Colors of War')], max_length=150, null=True)),
                ('notes', models.CharField(blank=True, max_length=150, null=True)),
                ('rewers', models.ImageField(blank=True, null=True, upload_to='')),
                ('dutch_direction', models.CharField(blank=True, choices=[('N', 'North'), ('NE', 'Northeast'), ('E', 'East'), ('SE', 'Southeast'), ('S', 'South'), ('SW', 'Southwest'), ('W', 'West'), ('NW', 'Northwest')], max_length=2, null=True)),
                ('english_direction', models.CharField(blank=True, choices=[('N', 'North'), ('NE', 'Northeast'), ('E', 'East'), ('SE', 'Southeast'), ('S', 'South'), ('SW', 'Southwest'), ('W', 'West'), ('NW', 'Northwest')], max_length=2, null=True)),
                ('french_direction', models.CharField(blank=True, choices=[('N', 'North'), ('NE', 'Northeast'), ('E', 'East'), ('SE', 'Southeast'), ('S', 'South'), ('SW', 'Southwest'), ('W', 'West'), ('NW', 'Northwest')], max_length=2, null=True)),
                ('spanish_direction', models.CharField(blank=True, choices=[('N', 'North'), ('NE', 'Northeast'), ('E', 'East'), ('SE', 'Southeast'), ('S', 'South'), ('SW', 'Southwest'), ('W', 'West'), ('NW', 'Northwest')], max_length=2, null=True)),
                ('pirateFrigate_direction', models.CharField(blank=True, choices=[('N', 'North'), ('NE', 'Northeast'), ('E', 'East'), ('SE', 'Southeast'), ('S', 'South'), ('SW', 'Southwest'), ('W', 'West'), ('NW', 'Northwest')], max_length=2, null=True)),
                ('pirateSloop_direction', models.CharField(blank=True, choices=[('N', 'North'), ('NE', 'Northeast'), ('E', 'East'), ('SE', 'Southeast'), ('S', 'South'), ('SW', 'Southwest'), ('W', 'West'), ('NW', 'Northwest')], max_length=2, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='GloryDeck',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('card', models.CharField(max_length=50, unique=True)),
                ('awers', models.ImageField(blank=True, null=True, upload_to='')),
                ('expansion', models.CharField(blank=True, choices=[('Seas of Glory', 'Seas of Glory'), ('Colors of War', 'Colors of War')], max_length=150, null=True)),
                ('notes', models.CharField(blank=True, max_length=150, null=True)),
                ('rewers', models.ImageField(blank=True, null=True, upload_to='')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='MissionsDeck',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('card', models.CharField(max_length=50, unique=True)),
                ('awers', models.ImageField(blank=True, null=True, upload_to='')),
                ('expansion', models.CharField(blank=True, choices=[('Seas of Glory', 'Seas of Glory'), ('Colors of War', 'Colors of War')], max_length=150, null=True)),
                ('notes', models.CharField(blank=True, max_length=150, null=True)),
                ('rewers', models.ImageField(blank=True, null=True, upload_to='')),
                ('earn', models.CharField(max_length=100)),
                ('requirements', models.CharField(max_length=100)),
                ('port', models.CharField(choices=[('Basse-Terre', 'Basse-Terre'), ('Bridgetown', 'Bridgetown'), ('Caracas', 'Caracas'), ('Cartagena', 'Cartagena'), ('Curacao', 'Curacao'), ('Havana', 'Havana'), ('Nassau', 'Nassau'), ('Old Providence', 'Old Providence'), ('Petite Goave', 'Petite Goave'), ('Port Royal', 'Port Royal'), ('San Juan', 'San Juan'), ('Santo Domingo', 'Santo Domingo'), ('St. John', 'St. John'), ('St. Maarten', 'St. Maarten'), ('Tortuga', 'Tortuga'), ('Trinidad', 'Trinidad')], max_length=100)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='RumorsDeck',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('card', models.CharField(max_length=50, unique=True)),
                ('awers', models.ImageField(blank=True, null=True, upload_to='')),
                ('expansion', models.CharField(blank=True, choices=[('Seas of Glory', 'Seas of Glory'), ('Colors of War', 'Colors of War')], max_length=150, null=True)),
                ('rewers', models.ImageField(blank=True, null=True, upload_to='')),
                ('require', models.CharField(max_length=200)),
                ('skill_test', models.CharField(choices=[('Scouting', 'Scouting'), ('Influence', 'Influence')], max_length=10)),
                ('notes', models.CharField(blank=True, max_length=150, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ShipsDeck',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('card', models.CharField(max_length=50, unique=True)),
                ('awers', models.ImageField(blank=True, null=True, upload_to='')),
                ('expansion', models.CharField(blank=True, choices=[('Seas of Glory', 'Seas of Glory'), ('Colors of War', 'Colors of War')], max_length=150, null=True)),
                ('notes', models.CharField(blank=True, max_length=150, null=True)),
                ('rewers', models.ImageField(blank=True, null=True, upload_to='')),
                ('toughness', models.IntegerField()),
                ('cargo', models.IntegerField()),
                ('crew', models.IntegerField()),
                ('cannons', models.IntegerField()),
                ('maneuverability', models.IntegerField()),
            ],
            options={
                'abstract': False,
            },
        ),
    ]