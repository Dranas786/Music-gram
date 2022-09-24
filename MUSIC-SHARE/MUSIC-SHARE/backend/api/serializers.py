from dataclasses import field
from pyexpat import model
from rest_framework import serializers
from .models import *


class PostsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Posts
        fields = "__all__"


class LikesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Likes
        fields = "__all__"


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('email', 'username', 'first_name', 'last_name',
                  'date_of_birth', 'password', 'biography', 'followers', 'following')


class UserRecommendationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserRecommendations
        fields = "__all__"


class AdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = Admin
        fields = "__all__"


class ModeratesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Moderates
        fields = "__all__"


class ManagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Manages
        fields = "__all__"


class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = "__all__"


class PlaylistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Playlist
        fields = "__all__"


class ContainsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contains
        fields = "__all__"


class ProductionLabelSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductionLabel
        fields = "__all__"


class ArtistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = "__all__"


class ProducerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producer
        fields = "__all__"


class MetadataSerializer(serializers.ModelSerializer):
    class Meta:
        model = Metadata
        fields = "__all__"


class ReleasesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Releases
        fields = "__all__"


class LikesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Likes
        fields = "__all__"


class FollowerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Follower
        fields = "__all__"
