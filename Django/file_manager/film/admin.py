from django.contrib import admin
from film.models import FilmInfo,PeopleInfo
# Register your models here.

admin.site.register(FilmInfo)
admin.site.register(PeopleInfo)