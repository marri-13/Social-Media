# core/models.py

from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User
from .user_models import User  

class User(AbstractUser):
    bio = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.username

class Post(models.Model):
    # Define fields for Post model
    title = models.CharField(max_length=255)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Comment(models.Model):
    # Define fields for Comment model
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    text = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment by {self.author.username} on {self.post.title}"
    class User(models.Model):user = models.ForeignKey(User, on_delete=models.CASCADE)
    class YourModelName(models.Model):user = models.ForeignKey(User, on_delete=models.CASCADE)
    

# Define other models like Like and Follow similarly
