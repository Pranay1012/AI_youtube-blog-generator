from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class BlogPost(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    youtube_title=models.CharField(max_length=255)
    youtube_url=models.URLField()
    transcript=models.TextField()
    gen_blog=models.TextField()
    created_time=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.youtube_title} by {self.user.username}"