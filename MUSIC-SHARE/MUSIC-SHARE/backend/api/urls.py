from django.urls import path
from .views import *

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    #path('user', UserView.as_view()),
    #path('user_list/', user_list),

    # returns user-list if it is GET
    # creates a new user if it is POST
    path("user/", UserAPIView.as_view()),

    # GET will give you user details
    # DELETE will delete the User from the database
    # PUT will update the user
    path("user/<str:pk>/", UserDetail.as_view()),

    # GET the song_id of all the liked music by the username
    # POST creates a new instance of username and song_id
    # because the user liked the song
    path("user/likemusic/<str:username>/", UserLikedMusic.as_view()),

    # DELETE removes the tupple with username and song_id
    # means that the user has unliked the song
    path("user/likemusic/<str:username>/<str:song_id>/",
         UserUnlikeMusic.as_view()),

    # GET gets the producer based on the producer_id
    # PUT updates the producer based on producer_id
    # DELETE deletes the producer tupple based on producer_id

    path("producer/<str:producer_id>/", ProducerDetail.as_view()),

    # GET gets the song info and meta info for that song_id
    path("song/<str:song_id>/", SongInfo.as_view()),

    # GET all the playlists of a user
    # POST creates a new playlist for the user
    path("playlist/<str:username>/", UserPlaylists.as_view()),

    # GET gets all the songs in a playlist
    # DELETE delete the playlist mentioned by the user
    path("playlist/<str:username>/<str:playlist_id>/",
         UserDelPlaylists.as_view()),

    # POST posts songs in a playlist
    # DELETE deletes a song from a playlist
    path("playlist/<str:username>/<str:playlist_id>/<str:song_id>/",
         EditPlayList.as_view()),

    # GET this will get song_id of all the posted music by the user
    # POST this will create a new user post
    path("posts/<str:username>/", UserPosts.as_view()),

    # DELETE unpost a song user posted
    path("posts/<str:username>/<str:song_id>/", UserUnposts.as_view()),


    # GET will check if the user already follows this other user
    path("followers/check/<str:username>/<str:otheruser_id>/",
         IfUserFollows.as_view()),


    # GET all the followers of the username
    path("followers/<str:username>/", UserFollowers.as_view()),

    # POST makes the user follow the other user
    # GET will get all the users which the current user is following
    # DELETE will unfollow a user
    path("following/<str:username>/<str:otheruser_id>/", UserFollowing.as_view()),

    # GET get the details of the artist
    path("artist/<str:artist_id>/", ArtistDetails.as_view()),

    # GET all the songs of an artist
    path("artist/allsongs/<str:artist_id>/", ArtistSongs.as_view()),

    # GET the song's Artist
    path("song/getartist/<str:song_id>/", SongArtists.as_view()),


]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_URL)
