from django.db import models


class Artist(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=500)
    year = models.DateField()
    picture = models.CharField(max_length=1000, default="Music/images/")

    def __str__(self):
        return self.name + ":" + self.description


class Album(models.Model):
    artist_id = models.ForeignKey('Artist', on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    release_date = models.DateField()
    # picture = models.FileField(max_length=1000, default="Music/images/")
    albumImage = models.FileField(upload_to="albumImages/", default="abc.jpg")

    def __str__(self):
        ret_str = "\n\nName:" + self.name + "\nRelease Date: " + \
            str(self.release_date)
        return ret_str


class Tracks(models.Model):
    album_id = models.ForeignKey('Album', on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    play_time = models.DurationField()
    lyric = models.FilePathField(path="/home/svshyam97/")
    picture = models.CharField(max_length=500, default="Music/images/")
    file_path = models.CharField(max_length=500)
    is_favourite = models.BooleanField(default="False")

    def __str__(self):
        return self.name + " " + str(self.play_time)


class Register(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=30, unique=True)
    username = models.CharField(max_length=20, unique=True)
    mobile_number = models.IntegerField(unique=True)
    age = models.IntegerField()

    def __str__(self):
        return self.username + " " + str(self.mobile_number)