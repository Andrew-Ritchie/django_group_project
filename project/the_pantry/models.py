from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

# Create your models here.
#basic models for posts and catagories created
#need to implement user_id from authetication section
class Category(models.Model):
    name = models.CharField(max_length=200, unique=True)

    class Meta:
        verbose_name_plural = "Catagories"

    def __str__(self): #python 2 unicode support
        return self.name

class Recipe(models.Model):
    title = models.CharField(max_length=200)
    category = models.ForeignKey(Category)
    content = models.TextField()
    created_on = models.DateTimeField(default=datetime.now)
    views = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)

    class Meta:
        verbose_name_plural = "Recipies"

    def __str__(self): #python 2 unicode support
        return self.title

class UserProfile(models.Model):
    # Link User profile to a User model instance
    user = models.OneToOneField(User)

    # Additional attributes
    picture = models.ImageField(upload_to='profile_images', blank = True)

    # Override __unicode__()
    def __str__(self):
        return self.user.username
