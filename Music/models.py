from django.db import models

class Artist(models.Model):
	name=models.CharField(max_length=200)
	description=models.CharField(max_length=500)
	year=models.DateField()
	picture=models.CharField(max_length=1000, default="Music/images/")
	
	def __str__(self):
		return self.name+":"+self.description
	

class Album(models.Model):
	artist_id=models.ForeignKey('Artist', on_delete=models.CASCADE)
	name=models.CharField(max_length=200)
	release_date=models.DateField()
	picture=models.CharField(max_length=1000, default="Music/images/")

	def __str__(self):
		ret_str="\n\nName:"+self.name+"\nRelease Date: "+str(self.release_date)+"\nPicture: "+self.picture
		return ret_str


class Tracks(models.Model):
	album_id=models.ForeignKey('Album', on_delete=models.CASCADE)
	name=models.CharField(max_length=200)
	play_time=models.DurationField()
	lyric=models.FilePathField(path="/home/svshyam97/")
	picture = models.CharField(max_length=500, default="Music/images/")
	file_path = models.CharField(max_length=500)
	is_favourite = models.BooleanField(default="False")

	def __str__(self):
		return self.name+" "+str(self.play_time)
