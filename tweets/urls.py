from django.urls import path
from . import views

urlpatterns = [
    path("", views.AllTweet.as_view(
        {
            "get": "list",
            "post": "create"
        }
    )),
]
