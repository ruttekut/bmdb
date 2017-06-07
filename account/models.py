from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save


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


class UserProfile(models.Model):
    user = models.OneToOneField(User)
    description = models.CharField(max_length=1000)
    city = models.CharField(max_length=100)
    website = models.URLField(default='')
    phone = models.IntegerField(default=0)


def create_profile(sender, **kwargs):
    if kwargs['created']:
        user_profile = UserProfile.objects.create(user=kwargs['instance'])


post_save.connect(create_profile, sender=User)
