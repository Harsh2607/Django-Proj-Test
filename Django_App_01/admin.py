from django.contrib import admin
from Django_App_01.models import Musician, Album, Post, UserProfileInfo

# Register your models here.
# class AuthorAdmin(admin.ModelAdmin):
#     pass

admin.site.register(Musician)
admin.site.register(Album)
admin.site.register(Post)
admin.site.register(UserProfileInfo)