# Generated by Django 4.1.3 on 2022-12-22 11:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotelapp', '0006_alter_team_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='name',
            field=models.CharField(max_length=200),
        ),
    ]
