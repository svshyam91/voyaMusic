from django.db import models


class Artist(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=500)
    picture = models.CharField(max_length=1000, default="Music/images/")

    def __str__(self):
        return self.name


class Album(models.Model):
    artist_id = models.ForeignKey('Artist', on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    release_date = models.DateField()
    albumImage = models.FileField(upload_to="images/albumImages/", default="abc.jpg")

    def __str__(self):
        ret_str = "\n\nName:" + self.name
        return ret_str


class Tracks(models.Model):
    album_id = models.ForeignKey('Album', on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    play_time = models.DurationField()
    lyric = models.FileField(upload_to="songs/lyrics/")
    picture = models.FileField(upload_to="songs/images/")
    file_path = models.FileField(upload_to="songs/tracks/")
    is_favourite = models.BooleanField(default="False")

    def __str__(self):
        return self.name

class Singles(models.Model):
    song_name = models.CharField(max_length=200)
    song_lyrics = models.FileField(upload_to="songs/lyrics/", null=True, blank=True)
    song_image = models.FileField(upload_to="songs/images/", null=True, blank=True)
    song_file_path = models.FileField(upload_to="songs/tracks/")
    is_favourite = models.BooleanField(default="False")

    def __str__(self):
        return self.song_name

class Register(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=30, unique=True)
    username = models.CharField(max_length=20, unique=True)
    mobile_number = models.IntegerField(unique=True)
    age = models.IntegerField()

    def __str__(self):
        return self.username + " " + str(self.mobile_number)