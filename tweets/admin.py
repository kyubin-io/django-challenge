from django.contrib import admin
from .models import Tweet, Like


@admin.register(Tweet)
class TweetAdmin(admin.ModelAdmin):

    list_display = (
        "payload",
        "user",
        "like_count",
    )


@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    pass
