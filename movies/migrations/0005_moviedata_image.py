# Generated by Django 4.2 on 2023-04-05 13:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0004_moviedata_genre'),
    ]

    operations = [
        migrations.AddField(
            model_name='moviedata',
            name='image',
            field=models.ImageField(default='images/none/noimg.jpg', upload_to='images'),
        ),
    ]
