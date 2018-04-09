# Generated by Django 2.0.2 on 2018-04-09 19:31

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('results', '0002_auto_20180409_1928'),
    ]

    operations = [
        migrations.RenameField(
            model_name='events',
            old_name='time',
            new_name='time_begin',
        ),
        migrations.AddField(
            model_name='events',
            name='time_end',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
