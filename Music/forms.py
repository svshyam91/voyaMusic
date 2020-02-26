from django import forms


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
