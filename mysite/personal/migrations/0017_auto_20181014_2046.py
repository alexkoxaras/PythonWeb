# Generated by Django 2.1.1 on 2018-10-14 17:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('personal', '0016_auto_20181014_2017'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='game',
            options={'ordering': ['game_title']},
        ),
        migrations.AlterModelOptions(
            name='topic',
            options={'ordering': ['topic_entry'], 'verbose_name': 'Ενότητα', 'verbose_name_plural': 'Ενότητες'},
        ),
        migrations.AlterField(
            model_name='game',
            name='game_dateimported',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Ημερομηνία Ένταξης'),
        ),
    ]
