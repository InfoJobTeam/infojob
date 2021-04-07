from django.contrib import admin

from .models import AddFavoriteVacancy, AddFavoriteCv

class AddFavoriteVacancyAdmin(admin.ModelAdmin):
    # какие поля будут отображаться в админке
    list_display = ('id', 'vacancy')
    # какие поля будут ссылками на соответствующие модели
    list_display_links = ('id', 'vacancy')
    # какие поля будут участвовать в поиске
    search_fields = ('vacancy',)


class AddFavoriteCvAdmin(admin.ModelAdmin):
    # какие поля будут отображаться в админке
    list_display = ('id', 'cvs')
    # какие поля будут ссылками на соответствующие модели
    list_display_links = ('id', 'cvs')
    # какие поля будут участвовать в поиске
    search_fields = ('cvs',)



admin.site.register(AddFavoriteVacancy, AddFavoriteVacancyAdmin)
admin.site.register(AddFavoriteCv, AddFavoriteCvAdmin)
