# Generated by Django 4.2 on 2023-04-05 06:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0002_moviedata_duration_moviedata_rating'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='moviedata',
            name='duration',
        ),
        migrations.AddField(
            model_name='moviedata',
            name='total_duration',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='moviedata',
            name='rating',
            field=models.FloatField(default=0),
        ),
    ]
