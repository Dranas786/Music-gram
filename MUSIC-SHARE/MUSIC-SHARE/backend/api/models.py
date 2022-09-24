from distutils.command import upload
from email.policy import default
from http.client import HTTPResponse
import imp
from pickle import TRUE
from django.db import models
from django.utils.translation import gettext_lazy as gl
# Create your models here.


def uploadTo(instance, filename):
    return "posts/{filename}".format(filename=filename)


class User(models.Model):
    email = models.CharField(max_length=100)
    username = models.CharField(max_length=100, primary_key=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    password = models.CharField(max_length=100)
    biography = models.CharField(max_length=100)
    followers = models.IntegerField()
    following = models.IntegerField()

    def __str__(self) -> str:
        return self.name


class UserRecommendations(models.Model):
    username = models.CharField(max_length=100)
    uRecommendations = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.name


class Admin(models.Model):
    permissions = models.CharField(max_length=20, default="none")
    admin_id = models.CharField(max_length=10, primary_key=True, default="-1")

    def __str__(self) -> str:
        return self.name


class Moderates(models.Model):
    admin_id = models.CharField(max_length=10, default="-1")
    song_id = models.CharField(max_length=10, default="-1")

    def __str__(self) -> str:
        return self.name


class Manages(models.Model):
    admin_id = models.CharField(max_length=10, default="-1")
    username = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.name


class Song(models.Model):
    song_id = models.CharField(max_length=10, primary_key=TRUE, default="-1")
    title = models.CharField(max_length=20, default="unknown")
    duration = models.IntegerField(null=True)

    def __str__(self) -> str:
        return self.name


class Likes(models.Model):
    username = models.CharField(max_length=100, default="unknown")
    song_id = models.CharField(max_length=10, default="-1")

    def __str__(self) -> str:
        return self.name


class Posts(models.Model):
    username = models.CharField(max_length=100, default="unknown")
    song_id = models.CharField(max_length=10, default="-1")

    def __str__(self) -> str:
        return self.name


class Playlist(models.Model):
    playlist_id = models.CharField(
        max_length=10, primary_key=TRUE, default="-1")
    username = models.CharField(max_length=100)
    playlist_name = models.CharField(max_length=10, default="unknown")

    def __str__(self) -> str:
        return self.name


class Contains(models.Model):
    song_id = models.CharField(max_length=10, default="-1")
    playlist_id = models.CharField(max_length=10, default="-1")
    username = models.CharField(max_length=10, default="-1")

    def __str__(self) -> str:
        return self.name


class ProductionLabel(models.Model):
    name = models.CharField(max_length=20, primary_key=True, default="-1")

    def __str__(self) -> str:
        return self.name


class Artist(models.Model):
    name = models.CharField(max_length=20, default="unknown")
    artist_id = models.CharField(
        max_length=10, primary_key=True, default="-1")
    p_name = models.CharField(max_length=10, default="-1")

    def __str__(self) -> str:
        return self.name


class Producer(models.Model):
    name = models.CharField(max_length=20, default="unknown")
    producer_id = models.CharField(
        max_length=10, primary_key=True, default="-1")
    p_name = models.CharField(max_length=10, default="-1")

    def __str__(self) -> str:
        return self.name


class Metadata(models.Model):
    mode = models.CharField(max_length=10, default="unknown")
    loudness = models.CharField(max_length=10, default="unknown")
    tempo = models.CharField(max_length=10, default="unknown")
    genre = models.CharField(max_length=20, default="unknown")
    acousticness = models.CharField(max_length=10, default="unknown")
    key = models.CharField(max_length=10, primary_key=True, default="-1")
    danceability = models.CharField(max_length=10, default="unknown")
    duration_ms = models.IntegerField(default=-1)
    energy = models.CharField(max_length=10, default="unknown")
    instrumentalness = models.CharField(max_length=10, default="unknown")
    liveness = models.CharField(max_length=10, default="unknown")
    speechiness = models.CharField(max_length=10, default="unknown")
    time_signature = models.CharField(max_length=10, default="unknown")
    valence = models.CharField(max_length=10, default="unknown")

    def __str__(self) -> str:
        return self.name


class Releases(models.Model):
    song_id = models.CharField(max_length=10, default="-1")
    artist_id = models.CharField(max_length=10, default="-1")
    p_name = models.CharField(max_length=10, default="-1")

    def __str__(self) -> str:
        return self.name


class Follower(models.Model):
    follower_id = models.CharField(max_length=10)
    user_id = models.CharField(max_length=10)

    def __str__(self) -> str:
        return self.name
