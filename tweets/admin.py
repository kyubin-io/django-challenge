from django.contrib import admin
from .models import Tweet, Like


@admin.register(Tweet)
class TweetAdmin(admin.ModelAdmin):
    list_display = ("payload", "user", "like_count", "created_at", "updated_at", )

    search_fields = ("payload", "user__name", )


@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    list_display = ("user", "tweet",  )

    search_fields = ("user__name", )
