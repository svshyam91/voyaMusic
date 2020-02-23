from django.conf.urls import url
from django.urls import path
from . import views

app_name = "Music"

urlpatterns = [
	# /music/
	path('',views.index, name='index'),

	# /music/album/
	path('album/',views.album, name='album'),

	# /music/album/702/
	path('album/<int:album_id>/',views.album_details, name='album_details'),
	
	# /music/artist/
	path('artist/', views.artist, name='artist'),

	# /music/artist/123/
	path('artist/<int:artist_id>/',views.artist_details, name='artist_details'),

	# /music/track/
	path('track/', views.track, name='track'),

	# /music/album/702/favourite
	path('album/<int:album_id>/favourite',views.favourite, name='favourite'),

	# /music/logIn/
	path('logIn', views.logIn, name="logIn"),

	# /music/logOut
	path('logOut', views.logOut, name="logOut"),

	# /music/register/
	path('register', views.register, name="register"),
]
