# Generated by Django 3.2.16 on 2022-10-17 10:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('course_live', '0002_auto_20220617_1822'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='historicalcourseliveconfiguration',
            options={'get_latest_by': ('history_date', 'history_id'), 'ordering': ('-history_date', '-history_id'), 'verbose_name': 'historical course live configuration', 'verbose_name_plural': 'historical course live configurations'},
        ),
    ]
