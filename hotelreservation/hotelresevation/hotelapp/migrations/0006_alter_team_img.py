# Generated by Django 4.1.3 on 2022-12-22 05:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotelapp', '0005_alter_team_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='img',
            field=models.ImageField(upload_to='images'),
        ),
    ]
