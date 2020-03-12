from django.contrib import admin

# Register your models here.
from .models import Artist, Album, Tracks, Register, Singles

admin.site.register(Artist)
admin.site.register(Album)
admin.site.register(Tracks)
admin.site.register(Register)
admin.site.register(Singles)
