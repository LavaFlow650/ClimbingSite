# Generated by Django 5.1 on 2024-08-26 21:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('routesetting', '0002_alter_route_options_rename_grade_route_grade_num_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='route',
            name='location',
            field=models.PositiveSmallIntegerField(blank=True, null=True),
        ),
    ]
