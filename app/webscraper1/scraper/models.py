from django.db import models


# Create your models here.
class Movies(models.Model):
    movie_name = models.CharField(max_length=200)
    director_name = models.CharField(max_length=200)
    writers_name = models.CharField(max_length=250)
    description = models.TextField()
    tagline = models.CharField(max_length=350)
    created_date = models.TimeField()

    def __str__(self):
        return self.movie_name

    class Meta:
        unique_together = (('movie_name'),)


class Reviews(models.Model):
    movie_name = models.CharField(max_length=200)
    subject = models.TextField()
    reviews = models.TextField()

    def __str__(self):
        return self.movie_name


class TopCast(models.Model):
    movie_name = models.CharField(max_length=200)
    actor_name = models.CharField(max_length=200)
    character_name = models.CharField(max_length=200)

    def __str__(self):
        return self.movie_name
