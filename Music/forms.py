from django import forms
from .models import Album


class Account(forms.Form):
    firstname = forms.CharField(label="First Name", max_length=50)
    lastname = forms.CharField(label="Last Name", max_length=50)
    email = forms.EmailField(label="Email", max_length=50)
    username = forms.CharField(label="Username", max_length=20)
    password = forms.CharField(
        label="Password", max_length=30, widget=forms.PasswordInput)
    mobileNumber = forms.IntegerField(label="Mobile Number")
    age = forms.IntegerField(label="Age")


class Login(forms.Form):
    username = forms.CharField(label="Username", max_length=50)
    password = forms.CharField(
        label="Password", max_length=30, widget=forms.PasswordInput)


class AddAlbum(forms.Form):
    albumName = forms.CharField(label="Album Name:", max_length=100)
    releaseYear = forms.DateField(label="Release Year:")
    albumPicture = forms.FileField()


class AddArtist(forms.Form):
    artistName = forms.CharField(label="Artist Name:", max_length=100)
    artistDescrip = forms.CharField(label="Artist Description:", max_length=100)
    artistPicture = forms.FileField()


class AddSong(forms.Form):

    # Get all album names and insert in tuple as tuple(value,label)
    allAlbums = Album.objects.all()
    ALBUMNAMES = (('Select','Select'),)
    for album in allAlbums:
        ALBUMNAMES = ALBUMNAMES+((album.id,album.name),)

    # ALBUMNAMES = (('Option1','1'),('Option2','Option1'),('Option3',))
    albumId = forms.ChoiceField(label="Select Album", choices=ALBUMNAMES)
    songName = forms.CharField(label="Song Name ", max_length=100)
    playTime = forms.DurationField(label="Play time ")
    releaseDate = forms.DateField(label="Song Release Date ")
    lyricsFile = forms.FileField(label="Lyrics File ")
    songImage = forms.FileField(label="Song Image ")
    songFile = forms.FileField(label="Song File ")


class AddSingles(forms.Form):
    ''' This form is to add singles '''

    song_name = forms.CharField(label="Song Name", max_length=200)
    song_lyrics = forms.FileField(label="Lyrics File", required=False)
    song_image = forms.FileField(label="Song Image File", required=False)
    song_file_path = forms.FileField(label="Song File")