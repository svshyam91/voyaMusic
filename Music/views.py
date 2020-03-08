from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import Artist, Album, Tracks, Register
from django.http import Http404
from django.urls import reverse
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from .forms import Account, Login, AddAlbum, AddArtist, AddSong
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
    context = {"all_artist": all_artist}
    # return HttpResponse(template.render(context, request))
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
        return render(request, "Music/album_details.html", {
            "album": album,
            "error_message": "You didn't select a valid track."})
    else:
        if selected_track.is_favourite:
            selected_track.is_favourite = False
        else:
            selected_track.is_favourite = True
        selected_track.save()

        return HttpResponseRedirect(reverse("Music:album_details", args=(album.id,)))


# /music/register
def register(request):
    if request.method == "POST":
        registerForm = Account(request.POST)
        if registerForm.is_valid():
            firstname = registerForm.cleaned_data["firstname"]
            lastname = registerForm.cleaned_data["lastname"]
            email = registerForm.cleaned_data["email"]
            username = registerForm.cleaned_data["username"]
            password = registerForm.cleaned_data["password"]
            mobileNumber = registerForm.cleaned_data["mobileNumber"]
            age = registerForm.cleaned_data["age"]

            # Storing data in database
            reg = Register()
            reg.first_name = firstname
            reg.last_name = lastname
            reg.username = username
            reg.email = email
            reg.age = age
            reg.mobile_number = mobileNumber
            reg.save()

            # Creating user
            user = User.objects.create_user(
                username=username, password=password,
                first_name=firstname, last_name=lastname, email=email)
            user.save()

            return HttpResponseRedirect(reverse("Music:index"))

    else:
        registerForm = Account()

    return render(request, "Music/register.html", {"registerForm": registerForm})


# /music/logIn
def logIn(request):
    if request.method == "POST":
        loginForm = Login(request.POST)     # Bound Form
        if loginForm.is_valid():
            username = loginForm.cleaned_data["username"]
            password = loginForm.cleaned_data["password"]
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect(reverse("Music:index"))
            else:
                return render(request, "Music/logIn.html", {
                    "loginForm": loginForm, "error_message": "Invalid Login"})
    else:
        # Unbound form
        loginForm = Login()

    return render(request, "Music/logIn.html", {"loginForm": loginForm})


def logOut(request):
    logout(request)
    return HttpResponseRedirect(reverse("Music:index"))


# /music/profile
def profile(request):
    """ This view handles multiple forms in a way that first it checks 
        request.method == "POST" and only if its true then it handles forms.
        Next, it checks whether form IS VALID OR NOT. UNBOUND FORM WILL NOT BE VALID.
        So, it'll validate only one form which return True for is_valid()."""

    if request.user.is_authenticated:

        # For showing user profile
        account = Register.objects.get(username=request.user.get_username())

        # For showing all artists
        artists = Artist.objects.all()

        # For adding album
        if request.method == "POST":
            albumForm = AddAlbum(request.POST, request.FILES)      # Bound Form
            if albumForm.is_valid():
                """ If artistForm is not valid then it will check next form"""
                
                artistId = request.POST.get("artistId")
                albumName = albumForm.cleaned_data["albumName"]
                releaseYear = albumForm.cleaned_data["releaseYear"]
                albumImage = request.FILES["albumPicture"]

                # Storing album in database
                artist = Artist.objects.get(id=artistId)
                album = Album(artist_id=artist,
                              name=albumName, release_date=releaseYear,
                              albumImage=albumImage)
                album.save()

                return render(request, "Music/profile.html", {
                    "username": request.user.get_username(),
                    "account": account})
        else:
            # Unbound Form
            albumForm = AddAlbum()
        # End of adding album

        # Adding Artist
        if request.method == "POST":
            """ If artistForm is not valid then it will check next form"""

            artistForm = AddArtist(
                request.POST, request.FILES)     # Bound Form
            if artistForm.is_valid():
                artistName = artistForm.cleaned_data["artistName"]
                artistDescrip = artistForm.cleaned_data["artistDescrip"]
                artistPicture = request.FILES["artistPicture"]

                # Storing artist in Database
                newArtist = Artist(name=artistName,
                                   description=artistDescrip, picture=artistPicture)
                newArtist.save()
                return render(request, "Music/profile.html", {
                    "username": request.user.get_username(),
                    "account": account,
                })
        else:
            artistForm = AddArtist()        # Unbound Form
        # End of adding Artist

        # Add Song
        if request.method == "POST":
            songForm = AddSong(request.POST, request.FILES)
            if songForm.is_valid():
                """ If albumForm is not valid then it'll check next form"""

                albumId = songForm.cleaned_data["albumId"]
                songName = songForm.cleaned_data["songName"]
                playTime = songForm.cleaned_data["playTime"]
                releaseDate = songForm.cleaned_data["releaseDate"]
                lyricsFile = request.FILES["lyricsFile"]
                songImage = request.FILES["songImage"]
                songFile = request.FILES["songFile"]

                # Storing song in Database
                album = Album.objects.get(id=albumId)    # Get album object associated with song
                song = Tracks(album_id=album,
                              name=songName, play_time=playTime, lyric=lyricsFile, 
                              picture=songImage, file_path=songFile, is_favourite="False"
                              )
                song.save()
                return HttpResponse("You have successfully uploaded song.")
        else:
            songForm = AddSong()
        # End of SongForm handling

        return render(request, "Music/profile.html", {
            "username": request.user.get_username(),
            "albumForm": albumForm,
            "artists": artists,
            "account": account,
            "artistForm": artistForm,
            "songForm": songForm, })
    else:
        # If the user is not logged in.
        return HttpResponseRedirect(reverse("Music:logIn"))
