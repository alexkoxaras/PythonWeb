# Generated by Django 2.1.1 on 2018-10-14 17:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('personal', '0017_auto_20181014_2046'),
    ]

    operations = [
        migrations.AlterField(
            model_name='topic',
            name='topic_anotherfield',
            field=models.DateField(auto_now=True, verbose_name='Ημερομηνία'),
        ),
    ]
