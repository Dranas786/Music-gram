from ast import Delete
from http.client import HTTPResponse

from django.db import connection
from .serializers import *
from .models import *

from django.http import HttpResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.parsers import MultiPartParser, FormParser

from rest_framework.views import APIView
# Create your views here.

# api for getting the user's liked musics

# to get the liked music of a user
# to update the liked music of a user

# update this api to implement username for searching the playlists


class IfUserFollows(APIView):
    def get(self, request, username, otheruser_id):
        try:
            Follower.objects.filter(
                user_id=username).get(follower_id=otheruser_id)
        except Follower.DoesNotExist:
            return Response({"alreadyFollows": False})

        return Response({"alreadyFollows": True})


class UserFollowing(APIView):
    def get(self, request, username, otheruser_id):
        following = Follower.objects.filter(follower_id=username)
        serializer = FollowerSerializer(following, many=True)
        return Response(serializer.data)

    # send the user who wants to follow as the follower_id
    # send the other user who will be followed as user_id
    def post(self, request, username, otheruser_id):
        serializer = FollowerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, username, otheruser_id):
        try:
            to_delete = Follower.objects.filter(
                user_id=otheruser_id).get(follower_id=username)
        except Follower.DoesNotExist:
            return HTTPResponse(status=status.HTTP_404_NOT_FOUND)

        to_delete.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class UserFollowers(APIView):
    def get(self, request, username):
        followers = Follower.objects.filter(user_id=username)
        serializer = FollowerSerializer(followers, many=True)
        return Response(serializer.data)


class EditPlayList(APIView):

    def post(self, request, playlist_id, song_id, username):
        serializer = ContainsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, playlist_id, song_id, username):
        try:
            song = Contains.objects.filter(
                playlist_id=playlist_id).filter(username=username).get(song_id=song_id)
        except Contains.DoesNotExist:
            return HTTPResponse(status=status.HTTP_404_NOT_FOUND)

        song.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class UserDelPlaylists(APIView):

    def get(self, request, playlist_id, username):
        songs = Contains.objects.filter(
            playlist_id=playlist_id).get(username=username)
        serializers = ContainsSerializer(songs, many=True)
        return Response(serializers.data)

    def delete(self, request, username, playlist_id):
        # removing playlist from the PlayLists
        try:
            playlist = Playlist.objects.filter(
                playlist_id=playlist_id).get(username=username)
        except Playlist.DoesNotExist:
            return HTTPResponse(status=status.HTTP_404_NOT_FOUND)
        playlist.delete()

        # removing all the songs in the playlist
        songs = Contains.objects.filter(playlist_id=playlist_id)
        for song in songs:
            song.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)


class UserPlaylists(APIView):
    def get(self, request, username):
        playlists = Playlist.objects.filter(username=username)
        serializer = PlaylistSerializer(playlists, many=True)
        return Response(serializer.data)

    def post(self, request, username):
        serializer = PlaylistSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserUnposts(APIView):
    def delete(self, request, username, song_id):
        try:
            post = Posts.objects.filter(username=username).get(song_id=song_id)
        except Posts.DoesNotExist:
            return HTTPResponse(status=status.HTTP_404_NOT_FOUND)

        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class UserPosts(APIView):
    def get(self, request, username):
        posted_songs = Posts.objects.filter(username=username)
        serializer = PostsSerializer(posted_songs, many=True)
        return Response(serializer.data)

    def post(self, request, username):
        serializer = PostsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# need to wait till the models are here
class SongInfo(APIView):
    def get(self, request, song_id):
        try:
            song = Song.objects.get(song_id=song_id)
        except Song.DoesNotExist:
            return HTTPResponse(status=status.HTTP_404_NOT_FOUND)
        try:
            metadata = Metadata.objects.get(key=song_id)
        except Metadata.DoesNotExist:
            return HTTPResponse(status=status.HTTP_404_NOT_FOUND)

        song_serializer = SongSerializer(song)
        metadata_serializer = MetadataSerializer(metadata)

        obj = {
            "song": song_serializer.data,
            "meta": metadata_serializer.data
        }
        return Response(obj)


class UserUnlikeMusic(APIView):
    def Delete(self, request, username, song_id):
        try:
            likedmusic = Likes.object.filter(
                username=username).get(song_id=song_id)
        except Likes.DoesNotExist:
            return HTTPResponse(status=status.HTTP_404_NOT_FOUND)

        likedmusic.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class UserLikedMusic(APIView):
    def get_liked_music(self, username):
        return Likes.objects.filter(username=username)

    def get(self, request, username):
        likedmusic = self.get_liked_music(username)
        serializer = LikesSerializer(likedmusic, many=True)
        return Response(serializer.data)

    def post(self, request, username):
        serializer = LikesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Using the classes for the apis
# this class does the same thing as the def user_list()


class UserAPIView(APIView):
    parser_classes = [MultiPartParser, FormParser]

    def get(self, request):
        # gets all the objects in the User relation
        users = User.objects.all()
        # converts all the objects to something python understands(dictionary)
        serializer = UserSerializer(users, many=True)
        # converts the dictionary into JSON and then send that as a response to the request
        # return JsonResponse(serializer.data, safe=False)
        # if you are using decorators and Response then you dont need the JSONResponse
        return Response(serializer.data)

    def post(self, request, format=None):
        print(request.data)
        # parses the JSON
        # data = JSONParser().parse(request)
        # dont need Parser when using decorators

        # serializes the parsed data into dictionary that python understands?
        # serializer = UserSerializer(data=data)
        # since we not using the parser. The decorators automatically Parse the json info?
        serializer = UserSerializer(data=request.data)

        # If the serialized data is valid we save it otherwise return JSON response with error
        if(serializer.is_valid()):
            serializer.save()
            # return JsonResponse(serializer.data, status=201)
            # using Response from rest_framework
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        # return JsonResponse(serializer.errors, status=400)
        # using Response from rest_framework
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# api view class for the function user_detail


class UserDetail(APIView):
    def get_user(self, username):
        try:
            return User.objects.get(pk=username)
        except User.DoesNotExist:
            return HTTPResponse(status=status.HTTP_404_NOT_FOUND)

    def get(self, req, pk):
        user = self.get_user(pk)
        serializer = UserSerializer(user)
        return Response(serializer.data)

    def put(self, req, pk):
        user = self.get_user(pk)
        serializer = UserSerializer(user, data=req.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, req, pk):
        user = self.get_user(pk)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ProducerDetail(APIView):
    def get_producer(self, producer_id):
        try:
            return Producer.objects.get(producer_id=producer_id)
        except Producer.DoesNotExist:
            return HTTPResponse(status=status.HTTP_404_NOT_FOUND)

    def get(self, req, producer_id):
        producer = self.get_producer(producer_id)
        serializer = ProducerSerializer(producer)
        return Response(serializer.data)

    def put(self, req, producer_id):
        producer = self.get_producer(producer_id)
        serializer = ProducerSerializer(producer, data=req.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, req, producer_id):
        producer = self.get_producer(producer_id)
        producer.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ArtistDetails(APIView):
    def get(self, request, artist_id):
        try:
            artist = Artist.objects.get(artist_id=artist_id)
        except Artist.DoesNotExist:
            return HTTPResponse(status=status.HTTP_404_NOT_FOUND)

        serializer = ArtistSerializer(artist)
        return Response(serializer.data)


class ArtistSongs(APIView):
    def get(self, request, artist_id):
        all_songs = Releases.objects.filter(artis_id=artist_id)
        serializer = ReleasesSerializer(all_songs, many=True)
        return Response(serializer.data)


class SongArtists(APIView):
    def get(self, request, song_id):
        all_artists = Releases.objects.filter(song_id=song_id)
        serializer = ReleasesSerializer(all_artists, many=True)
        return Response(serializer.data)
