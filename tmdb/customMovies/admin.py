from django.contrib import admin
from .models import Movie


# Register your models here.
class MovieAdmin(admin.ModelAdmin):
    readonly_fields = ('created','updated')

admin.site.register(Movie, MovieAdmin)
