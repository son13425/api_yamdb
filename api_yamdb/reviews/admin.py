from django.contrib import admin

from .models import Category, Comment, Genre, GenreTitle, Review, Title, CustomUser


admin.site.register(CustomUser)
admin.site.register(Category)
admin.site.register(Genre)
admin.site.register(Title)
admin.site.register(GenreTitle)
admin.site.register(Review)
admin.site.register(Comment) 
