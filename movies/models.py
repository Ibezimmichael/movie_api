from django.db import models

class MovieData(models.Model):
    title = models.CharField(max_length=250)
    total_duration = models.FloatField(default=0)
    rating = models.FloatField(default=0)
    genre = models.CharField(max_length=200, default='drama')
    image = models.ImageField(upload_to='images', default='images/none/noimg.jpg')

    def __str__(self) -> str:
        return self.title