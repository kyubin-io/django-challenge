from django.db import models

class Tweet(models.Model):

    """Model Definition for Tweet"""

    payload = models.TextField(max_length=180)
    user = models.ForeignKey("users.User", on_delete=models.CASCADE)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    def __str__(self):
        return self.name