from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save


class UserProfile(models.Model):
    user = models.OneToOneField(User)
    description = models.CharField(max_length=1000, blank=True)
    city = models.CharField(max_length=100, blank=True)
    website = models.URLField(default='', blank=True)
    phone = models.IntegerField(default=0, blank=True)


def create_profile(sender, **kwargs):
    if kwargs['created']:
        UserProfile.objects.create(user=kwargs['instance'])


post_save.connect(create_profile, sender=User)


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
    ratings = models.IntegerField(default=0)
    users = models.ManyToManyField(User)
    current_user = models.ForeignKey(User, related_name='owner', null=True)

    @classmethod
    def add_favorite(cls, current_user, new_book):
        book, created = cls.objects.get_or_create(
            current_user=current_user
        )
        book.users.add(new_book)

    @classmethod
    def remove_favorite(cls, current_user, new_book):
        book, created = cls.objects.get_or_create(
            current_user=current_user
        )
        book.users.remove(new_book)

    def __str__(self):
            return self.name
