from django.contrib import admin
from Endless.models import Post, ListUser, Comment, Like, UserConnection

# Register your models here.
admin.site.register(Post)
admin.site.register(ListUser)
admin.site.register(Comment)
admin.site.register(Like)
admin.site.register(UserConnection)