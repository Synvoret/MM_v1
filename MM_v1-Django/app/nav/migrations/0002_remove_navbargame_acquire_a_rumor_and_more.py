# Generated by Django 5.0 on 2024-03-14 05:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nav', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='navbargame',
            name='acquire_a_rumor',
        ),
        migrations.RemoveField(
            model_name='navbargame',
            name='back',
        ),
        migrations.RemoveField(
            model_name='navbargame',
            name='back_to_port',
        ),
        migrations.RemoveField(
            model_name='navbargame',
            name='blue_player_ship',
        ),
        migrations.RemoveField(
            model_name='navbargame',
            name='but_goods',
        ),
        migrations.RemoveField(
            model_name='navbargame',
            name='buy_ship_modification',
        ),
        migrations.RemoveField(
            model_name='navbargame',
            name='buy_special_weapon',
        ),
        migrations.RemoveField(
            model_name='navbargame',
            name='claim_a_mission',
        ),
        migrations.RemoveField(
            model_name='navbargame',
            name='dutch_ship',
        ),
        migrations.RemoveField(
            model_name='navbargame',
            name='e_direction',
        ),
        migrations.RemoveField(
            model_name='navbargame',
            name='end_turn',
        ),
        migrations.RemoveField(
            model_name='navbargame',
            name='english_ship',
        ),
        migrations.RemoveField(
            model_name='navbargame',
            name='fishing',
        ),
        migrations.RemoveField(
            model_name='navbargame',
            name='french_ship',
        ),
        migrations.RemoveField(
            model_name='navbargame',
            name='from_port',
        ),
        migrations.RemoveField(
            model_name='navbargame',
            name='gain_loyality',
        ),
        migrations.RemoveField(
            model_name='navbargame',
            name='get_favour',
        ),
        migrations.RemoveField(
            model_name='navbargame',
            name='green_player_ship',
        ),
        migrations.RemoveField(
            model_name='navbargame',
            name='large_pirate_ship',
        ),
        migrations.RemoveField(
            model_name='navbargame',
            name='merchant',
        ),
        migrations.RemoveField(
            model_name='navbargame',
            name='merchant_escort',
        ),
        migrations.RemoveField(
            model_name='navbargame',
            name='merchant_raid',
        ),
        migrations.RemoveField(
            model_name='navbargame',
            name='merchant_trade',
        ),
        migrations.RemoveField(
            model_name='navbargame',
            name='move',
        ),
        migrations.RemoveField(
            model_name='navbargame',
            name='n_direction',
        ),
        migrations.RemoveField(
            model_name='navbargame',
            name='ne_direction',
        ),
        migrations.RemoveField(
            model_name='navbargame',
            name='nw_direction',
        ),
        migrations.RemoveField(
            model_name='navbargame',
            name='player_colour',
        ),
        migrations.RemoveField(
            model_name='navbargame',
            name='port',
        ),
        migrations.RemoveField(
            model_name='navbargame',
            name='recruit',
        ),
        migrations.RemoveField(
            model_name='navbargame',
            name='red_player_ship',
        ),
        migrations.RemoveField(
            model_name='navbargame',
            name='repair',
        ),
        migrations.RemoveField(
            model_name='navbargame',
            name='s_direction',
        ),
        migrations.RemoveField(
            model_name='navbargame',
            name='scout',
        ),
        migrations.RemoveField(
            model_name='navbargame',
            name='se_direction',
        ),
        migrations.RemoveField(
            model_name='navbargame',
            name='sell_buy_ship',
        ),
        migrations.RemoveField(
            model_name='navbargame',
            name='sell_goods',
        ),
        migrations.RemoveField(
            model_name='navbargame',
            name='small_pirate_ship',
        ),
        migrations.RemoveField(
            model_name='navbargame',
            name='spanish_ship',
        ),
        migrations.RemoveField(
            model_name='navbargame',
            name='stash_gold',
        ),
        migrations.RemoveField(
            model_name='navbargame',
            name='sw_direction',
        ),
        migrations.RemoveField(
            model_name='navbargame',
            name='to_port',
        ),
        migrations.RemoveField(
            model_name='navbargame',
            name='to_sea_zone',
        ),
        migrations.RemoveField(
            model_name='navbargame',
            name='visit_location',
        ),
        migrations.RemoveField(
            model_name='navbargame',
            name='visit_shipyard',
        ),
        migrations.RemoveField(
            model_name='navbargame',
            name='w_direction',
        ),
        migrations.RemoveField(
            model_name='navbargame',
            name='yellow_player_ship',
        ),
        migrations.AddField(
            model_name='navbargame',
            name='player_blue',
            field=models.JSONField(blank=True, default=list, null=True),
        ),
        migrations.AddField(
            model_name='navbargame',
            name='player_green',
            field=models.JSONField(blank=True, default=list, null=True),
        ),
        migrations.AddField(
            model_name='navbargame',
            name='player_red',
            field=models.JSONField(blank=True, default=list, null=True),
        ),
        migrations.AddField(
            model_name='navbargame',
            name='player_yellow',
            field=models.JSONField(blank=True, default=list, null=True),
        ),
    ]
