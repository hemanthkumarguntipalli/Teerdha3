# Generated by Django 5.0.3 on 2024-03-27 07:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0017_hotel_boboffer_hotel_boboffer1_hotel_bobpolicy'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='kotak_offer',
            new_name='flights_kotak_offer',
        ),
        migrations.RenameModel(
            old_name='kotak_offer1',
            new_name='flights_kotak_offer1',
        ),
        migrations.RenameModel(
            old_name='kotak_terms',
            new_name='flights_kotak_terms',
        ),
        migrations.RenameModel(
            old_name='policy',
            new_name='flights_policy',
        ),
        migrations.RenameModel(
            old_name='policy1',
            new_name='flights_policy1',
        ),
        migrations.AlterModelTable(
            name='flights_kotak_offer',
            table='flights_kotak_offer',
        ),
        migrations.AlterModelTable(
            name='flights_kotak_offer1',
            table='flights_kotak_offer1',
        ),
        migrations.AlterModelTable(
            name='flights_kotak_terms',
            table='flights_kotak_terms',
        ),
        migrations.AlterModelTable(
            name='flights_policy',
            table='flights_policy',
        ),
        migrations.AlterModelTable(
            name='flights_policy1',
            table='flights_policy1',
        ),
    ]
