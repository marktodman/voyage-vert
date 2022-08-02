# Generated by Django 3.2.14 on 2022-08-02 20:08

import cloudinary.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Passenger',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=80)),
                ('last_name', models.CharField(max_length=80)),
                ('email', models.EmailField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Route',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('route_name', models.CharField(max_length=200, verbose_name='Route Name')),
                ('description', models.TextField()),
                ('duration', models.IntegerField()),
                ('distance', models.IntegerField()),
                ('featured_image', cloudinary.models.CloudinaryField(default='placeholder', max_length=255, verbose_name='Image')),
            ],
            options={
                'ordering': ['route_name'],
            },
        ),
        migrations.CreateModel(
            name='Trip',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('trip_name', models.CharField(max_length=200, verbose_name='Trip Name')),
                ('trip_date', models.DateField(verbose_name='Trip Date')),
                ('description', models.TextField()),
                ('number_passengers', models.IntegerField()),
                ('cabin_type', models.IntegerField(choices=[(0, 'Shared'), (1, 'Private')], default=0)),
                ('crew_option', models.IntegerField(choices=[(0, 'Crew'), (1, 'Passenger Only')], default=0)),
                ('sailing_exp', models.IntegerField(choices=[(0, 'None'), (1, 'Some'), (2, 'Lots')], default=0)),
                ('featured_image', cloudinary.models.CloudinaryField(default='placeholder', max_length=255, verbose_name='Image')),
                ('interest', models.ManyToManyField(blank=True, related_name='trip_interest', to='bookings.Passenger')),
                ('passenger', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='bookings.passenger')),
                ('route_name', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='bookings.route')),
            ],
            options={
                'ordering': ['trip_date'],
            },
        ),
    ]
