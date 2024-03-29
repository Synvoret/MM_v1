# Generated by Django 5.0 on 2024-03-06 07:28

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dataset', '0077_alter_demandtokens_cargo'),
        ('game', '0092_alter_stackplayercargocards_cargo_card_1_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gamedemandtokens',
            name='basse_terre',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='demand_basse_terre', to='dataset.demandtokens'),
        ),
        migrations.AlterField(
            model_name='gamedemandtokens',
            name='bridgetown',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='demand_bridgetown', to='dataset.demandtokens'),
        ),
        migrations.AlterField(
            model_name='gamedemandtokens',
            name='caracas',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='demand_caracas', to='dataset.demandtokens'),
        ),
        migrations.AlterField(
            model_name='gamedemandtokens',
            name='cartagena',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='demand_cartagena', to='dataset.demandtokens'),
        ),
        migrations.AlterField(
            model_name='gamedemandtokens',
            name='curacao',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='demand_curacao', to='dataset.demandtokens'),
        ),
        migrations.AlterField(
            model_name='gamedemandtokens',
            name='gulf_city',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='demand_gulf_city', to='dataset.demandtokens'),
        ),
        migrations.AlterField(
            model_name='gamedemandtokens',
            name='havana',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='demand_havana', to='dataset.demandtokens'),
        ),
        migrations.AlterField(
            model_name='gamedemandtokens',
            name='nassau',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='demand_nassau', to='dataset.demandtokens'),
        ),
        migrations.AlterField(
            model_name='gamedemandtokens',
            name='old_providence',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='demand_old_providence', to='dataset.demandtokens'),
        ),
        migrations.AlterField(
            model_name='gamedemandtokens',
            name='petite_goave',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='demand_petite_goave', to='dataset.demandtokens'),
        ),
        migrations.AlterField(
            model_name='gamedemandtokens',
            name='port_royal',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='demand_port_royal', to='dataset.demandtokens'),
        ),
        migrations.AlterField(
            model_name='gamedemandtokens',
            name='san_juan',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='demand_san_juan', to='dataset.demandtokens'),
        ),
        migrations.AlterField(
            model_name='gamedemandtokens',
            name='santo_domingo',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='demand_santo_domingo', to='dataset.demandtokens'),
        ),
        migrations.AlterField(
            model_name='gamedemandtokens',
            name='st_john',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='demand_st_john', to='dataset.demandtokens'),
        ),
        migrations.AlterField(
            model_name='gamedemandtokens',
            name='st_maarten',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='demand_st_maarten', to='dataset.demandtokens'),
        ),
        migrations.AlterField(
            model_name='gamedemandtokens',
            name='tortuga',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='demand_tortuga', to='dataset.demandtokens'),
        ),
        migrations.AlterField(
            model_name='gamedemandtokens',
            name='trinidad',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='demand_trinidad', to='dataset.demandtokens'),
        ),
    ]
