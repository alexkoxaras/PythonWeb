# Generated by Django 2.1.1 on 2018-10-14 17:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('personal', '0018_auto_20181014_2048'),
    ]

    operations = [
        migrations.AlterField(
            model_name='topic',
            name='topic_anotherfield',
            field=models.DateField(auto_now_add=True, verbose_name='Ημερομηνία'),
        ),
    ]
