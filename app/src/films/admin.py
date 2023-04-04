from django.contrib import admin

from .models import Film, UserFilmRelation, Category


@admin.register(Film)
class AdminFilm(admin.ModelAdmin):
    pass


@admin.register(UserFilmRelation)
class RelationAdmin(admin.ModelAdmin):
    pass


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass
