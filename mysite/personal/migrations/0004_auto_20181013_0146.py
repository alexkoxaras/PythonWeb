# Generated by Django 2.1.1 on 2018-10-12 22:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('personal', '0003_auto_20181013_0135'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='game_dateimported',
            field=models.DateField(blank=True, verbose_name='Ημερομηνία Ένταξης'),
        ),
        migrations.AlterField(
            model_name='game',
            name='game_environment',
            field=models.CharField(blank=True, max_length=30, verbose_name='Τόπος εκπαίδευσης'),
        ),
        migrations.AlterField(
            model_name='game',
            name='game_image',
            field=models.FilePathField(blank=True, verbose_name='Εικόνα'),
        ),
        migrations.AlterField(
            model_name='game',
            name='game_materials',
            field=models.CharField(blank=True, max_length=30, verbose_name='Υλικά που απαιτούνται'),
        ),
        migrations.AlterField(
            model_name='game',
            name='game_maxpersons',
            field=models.IntegerField(blank=True, verbose_name='Μέγιστος αρ. ατόμων'),
        ),
        migrations.AlterField(
            model_name='game',
            name='game_maxteams',
            field=models.IntegerField(blank=True, verbose_name='Μέγιστος αρ. ομάδων'),
        ),
        migrations.AlterField(
            model_name='game',
            name='game_minfacilitators',
            field=models.IntegerField(blank=True, verbose_name='Αριθμός ελάχιστων Facilitators'),
        ),
        migrations.AlterField(
            model_name='game',
            name='game_minpersons',
            field=models.IntegerField(blank=True, verbose_name='Ελάχιστος αρ. ατόμων'),
        ),
        migrations.AlterField(
            model_name='game',
            name='game_minteams',
            field=models.IntegerField(blank=True, verbose_name='Ελάχιστος αρ. ομάδων'),
        ),
        migrations.AlterField(
            model_name='game',
            name='game_portable',
            field=models.CharField(blank=True, max_length=30, verbose_name='Φορητότητα'),
        ),
        migrations.AlterField(
            model_name='game',
            name='game_subjects',
            field=models.ManyToManyField(blank=True, to='personal.Topics', verbose_name='Θεματολογια'),
        ),
        migrations.AlterField(
            model_name='game',
            name='game_subtitle',
            field=models.CharField(blank=True, max_length=30, verbose_name='Υπότιτλος'),
        ),
        migrations.AlterField(
            model_name='game',
            name='game_timeneeded',
            field=models.CharField(blank=True, max_length=30, verbose_name='Ελάχιστος χρόνος'),
        ),
        migrations.AlterField(
            model_name='game',
            name='game_title',
            field=models.CharField(blank=True, max_length=30, verbose_name='Τίτλος'),
        ),
    ]
