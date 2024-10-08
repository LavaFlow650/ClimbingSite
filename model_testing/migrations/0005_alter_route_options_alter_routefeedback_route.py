# Generated by Django 5.1 on 2024-08-24 06:15

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('model_testing', '0004_routefeedback'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='route',
            options={'ordering': ['grade_num']},
        ),
        migrations.AlterField(
            model_name='routefeedback',
            name='route',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='model_testing.route'),
        ),
    ]
