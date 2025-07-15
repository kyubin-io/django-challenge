from django.contrib import admin
from .models import Tweet, Like


class elonMusk(admin.SimpleListFilter):

    title = "Filter by Elon Musk"

    parameter_name = "musk"

    def lookups(self, request, model_admin):
        return [
            ("musk", "Elon Musk"),
            ("no_musk", "No Musk"),
        ]
    
    def queryset(self, request, tweets):
        musk = self.value()
        if musk == "musk":
            return tweets.filter(payload__icontains="Elon Musk")
        elif musk == "no_musk":
            tweets.exclude(payload__icontains="Elon Musk")
        else:
            tweets



@admin.register(Tweet)
class TweetAdmin(admin.ModelAdmin):
    list_display = ("payload", "user", "like_count", "created_at", "updated_at", )

    search_fields = ("payload", "user__name", )

    list_filter = (elonMusk, "created_at", )


@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    list_display = ("user", "tweet",  )

    search_fields = ("user__name", )

    list_filter = ("created_at", )
