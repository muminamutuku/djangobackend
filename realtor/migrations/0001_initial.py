# Generated by Django 4.0 on 2022-11-13 15:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ForRent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(max_length=50)),
                ('coverPhoto', models.ImageField(blank='false', null='false', upload_to='uploads/images')),
                ('otherPhotos', models.ImageField(blank='false', null='false', upload_to='', verbose_name='uploads/photos')),
                ('purpose', models.CharField(max_length=50)),
                ('furnishingStatus', models.CharField(max_length=50)),
                ('housetype', models.CharField(max_length=50)),
                ('description', models.TextField(blank=True, max_length=1000)),
                ('rooms', models.CharField(max_length=50)),
                ('amenities', models.CharField(max_length=5000)),
                ('bathrooms', models.CharField(max_length=50)),
                ('ownerId', models.CharField(max_length=500)),
                ('rentamount', models.IntegerField(blank=True)),
                ('rentFrequency', models.CharField(max_length=50)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ForSale',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(max_length=50)),
                ('coverPhoto', models.ImageField(blank='false', null='false', upload_to='uploads/images')),
                ('otherPhotos', models.ImageField(blank='false', null='false', upload_to='', verbose_name='uploads/photos')),
                ('purpose', models.CharField(max_length=50)),
                ('furnishingStatus', models.CharField(max_length=50)),
                ('housetype', models.CharField(max_length=50)),
                ('description', models.TextField(blank=True, max_length=1000)),
                ('rooms', models.CharField(max_length=50)),
                ('amenities', models.CharField(max_length=5000)),
                ('bathrooms', models.CharField(max_length=50)),
                ('ownerId', models.CharField(max_length=500)),
                ('price', models.IntegerField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='PhoneNumber',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.IntegerField()),
            ],
        ),
    ]
