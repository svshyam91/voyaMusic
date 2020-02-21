from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .models import Artist, Album, Tracks
from django.http import Http404
from django.urls import reverse
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
#from django.template import loader


# /music/
def index(request):
	albums = Album.objects.all()
	context = {"albums": albums}
	return render(request, "Music/index.html", context)
	

# /music/album/
def album(request):
	all_album = Album.objects.all()
	context = {"all_album": all_album}
	return render(request, "Music/album.html", context)


# /music/album/123/
def album_details(request, album_id):
	album = Album.objects.get(id=album_id)
	context = {"album": album}
	return render(request, "Music/album_details.html", context)


# /music/artist/
def artist(request):
	all_artist = Artist.objects.all()
	#template = loader.get_template("Music/index.html")
	context = { "all_artist": all_artist }
	#return HttpResponse(template.render(context, request))
	return render(request, "Music/artist.html", context)


# /music/artist/343/
def artist_details(request, artist_id):
	artist = get_object_or_404(Artist, id=artist_id)
	# artist = Artist.objects.get(id=artist_id)
	context = {"artist": artist}
	return render(request, "Music/artist_detail.html", context)
	

# /music/track/12
def track(request):
	try:
		tracks = Tracks.objects.all()
	except Tracks.DoesNotExist: 
		raise Http404("Album Does Not Exist")
	context = {"tracks": tracks}
	return render(request, "Music/track.html", context)


# /music/album/702/favourite
def favourite(request, album_id):

	# Get the album.id of the selected track
	album = get_object_or_404(Album, id=album_id)
	try:
		# Get the selected track of album.id. If present in DB then proceed
		selected_track = album.tracks_set.get(id=request.POST['track'])
	except (KeyError, Tracks.DoesNotExist):
		return render(request, "Music/album_details.html", { "album": album,
			"error_message": "You didn't select a valid track." })
	else:
		if selected_track.is_favourite:
			selected_track.is_favourite = False
		else:
			selected_track.is_favourite = True
		selected_track.save()

		return HttpResponseRedirect(reverse("Music:album_details", args=(album.id,)))


# /music/logIn
def logIn(request):
	if request.method == POST:
		loginForm = Login(request.POST)		# Bound Form
		if loginForm.is_valid():
			username = loginForm.cleaned_data["username"]
			password = loginForm.cleaned_data["password"]
			user = authenticate(username = username, password=password)
			login(request, user)
			return HttpResponseRedirect(request.path_info)
	else:
		# Unbound form
		loginForm = Login()

	return render(request, "Music/logIn.html", {"loginForm": loginForm})
