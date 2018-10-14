# Generated by Django 2.1.1 on 2018-10-12 22:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('personal', '0004_auto_20181013_0146'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='game',
            name='game_subjects',
        ),
        migrations.AddField(
            model_name='game',
            name='game_subjects',
            field=models.OneToOneField(default=2, on_delete=django.db.models.deletion.CASCADE, to='personal.Topics', verbose_name='Θεματολογια'),
            preserve_default=False,
        ),
    ]
