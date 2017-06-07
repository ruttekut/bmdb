from django.db import models


# Create your models here.
class Books(models.Model):
    GENRES = (
        ('romance', 'Romance'),
        ('science', 'Science'),
        ('romans', 'Romans'),
    )
    genre = models.CharField(max_length=20, choices=GENRES, null=True)
    name = models.CharField(max_length=1000)
    author = models.CharField(max_length=1000)
    description = models.TextField()
    img = models.ImageField()

    def __str__(self):
            return self.name
