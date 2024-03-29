# Generated by Django 5.0 on 2024-03-06 08:21

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dataset', '0077_alter_demandtokens_cargo'),
        ('game', '0093_alter_gamedemandtokens_basse_terre_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gamedemandtokens',
            name='basse_terre',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='basse_terre_demand_tokens', to='dataset.demandtokens'),
        ),
        migrations.AlterField(
            model_name='gamedemandtokens',
            name='bridgetown',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='bridgetown_demand_tokens', to='dataset.demandtokens'),
        ),
        migrations.AlterField(
            model_name='gamedemandtokens',
            name='caracas',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='caracas_demand_tokens', to='dataset.demandtokens'),
        ),
        migrations.AlterField(
            model_name='gamedemandtokens',
            name='cartagena',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='cartagena_demand_tokens', to='dataset.demandtokens'),
        ),
        migrations.AlterField(
            model_name='gamedemandtokens',
            name='curacao',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='curacao_demand_tokens', to='dataset.demandtokens'),
        ),
        migrations.AlterField(
            model_name='gamedemandtokens',
            name='gulf_city',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='gulf_city_demand_tokens', to='dataset.demandtokens'),
        ),
        migrations.AlterField(
            model_name='gamedemandtokens',
            name='havana',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='havana_demand_tokens', to='dataset.demandtokens'),
        ),
        migrations.AlterField(
            model_name='gamedemandtokens',
            name='nassau',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='nassau_demand_tokens', to='dataset.demandtokens'),
        ),
        migrations.AlterField(
            model_name='gamedemandtokens',
            name='old_providence',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='old_providence_demand_tokens', to='dataset.demandtokens'),
        ),
        migrations.AlterField(
            model_name='gamedemandtokens',
            name='petite_goave',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='petite_goave_demand_tokens', to='dataset.demandtokens'),
        ),
        migrations.AlterField(
            model_name='gamedemandtokens',
            name='port_royal',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='port_royal_demand_tokens', to='dataset.demandtokens'),
        ),
        migrations.AlterField(
            model_name='gamedemandtokens',
            name='san_juan',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='san_juan_demand_tokens', to='dataset.demandtokens'),
        ),
        migrations.AlterField(
            model_name='gamedemandtokens',
            name='santo_domingo',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='santo_domingo_demand_tokens', to='dataset.demandtokens'),
        ),
        migrations.AlterField(
            model_name='gamedemandtokens',
            name='st_john',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='st_john_demand_tokens', to='dataset.demandtokens'),
        ),
        migrations.AlterField(
            model_name='gamedemandtokens',
            name='st_maarten',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='st_maarten_demand_tokens', to='dataset.demandtokens'),
        ),
        migrations.AlterField(
            model_name='gamedemandtokens',
            name='tortuga',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='tortuga_demand_tokens', to='dataset.demandtokens'),
        ),
        migrations.AlterField(
            model_name='gamedemandtokens',
            name='trinidad',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='trinidad_demand_tokens', to='dataset.demandtokens'),
        ),
    ]
