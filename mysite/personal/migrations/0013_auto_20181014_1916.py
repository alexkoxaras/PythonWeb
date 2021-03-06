# Generated by Django 2.1.1 on 2018-10-14 16:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('personal', '0012_auto_20181013_2139'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='game_link',
            field=models.CharField(blank=True, max_length=255, verbose_name='Οδηγίες'),
        ),
        migrations.AlterField(
            model_name='game',
            name='game_environment',
            field=models.CharField(blank=True, max_length=50, verbose_name='Τόπος εκπαίδευσης'),
        ),
        migrations.AlterField(
            model_name='game',
            name='game_materials',
            field=models.CharField(blank=True, max_length=100, verbose_name='Υλικά που απαιτούνται'),
        ),
    ]
