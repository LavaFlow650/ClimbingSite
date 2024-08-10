# Generated by Django 5.0.7 on 2024-08-06 07:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('routesetting', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Route',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('grade', models.SmallIntegerField(max_length=2)),
                ('location', models.PositiveSmallIntegerField(max_length=1)),
                ('color', models.CharField(choices=[('R', 'Red'), ('O', 'Orange'), ('Y', 'Yellow'), ('LG', 'Light green'), ('DG', 'Dark green'), ('Bu', 'Blue'), ('Pu', 'Purple'), ('Bk', 'Black'), ('Pi', 'Pink'), ('W', 'White')], default='R', max_length=2)),
                ('name', models.CharField(max_length=100)),
                ('setter', models.CharField(choices=[('K', 'KB'), ('A', 'APE'), ('O', 'OK'), ('T', 'TOPS'), ('F', 'firewx')], default='K', max_length=2)),
                ('date_set', models.DateField()),
                ('date_logged', models.DateTimeField()),
                ('archived', models.BooleanField()),
                ('archived_date', models.DateTimeField(null=True)),
            ],
        ),
    ]
