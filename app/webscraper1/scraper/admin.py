from django.contrib import admin
from .models import Movies,Reviews,TopCast


# Register your models here.
class MovieAdmin(admin.ModelAdmin):
    list_display = ("movie_name", "director_name", "writers_name", "description", "tagline",'created_date')
    list_filter = ("movie_name",)


class TopCastAdmin(admin.ModelAdmin):
    list_display = ('movie_name', 'actor_name', 'character_name')
    list_filter = ("movie_name",)


class ReviewAdmin(admin.ModelAdmin):
    list_display = ('movie_name', 'subject', 'reviews')


admin.site.register(Movies, MovieAdmin)
admin.site.register(TopCast, TopCastAdmin)
admin.site.register(Reviews, ReviewAdmin)
