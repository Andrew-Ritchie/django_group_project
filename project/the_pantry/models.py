from django.db import models
from datetime import datetime

# Create your models here.
#basic models for posts and catagories created
#need to implement user_id from authetication section
class Category(models.Model):
    name = models.CharField(max_length=200, unique=True)

    class Meta:
        verbose_name_plural = "Catagories"

class Recipe(models.Model):
    title = models.CharField(max_length=200)
    category = models.ForeignKey(Category)
    content = models.TextField()
    created_on = models.DateTimeField(default=datetime.now)
    views = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)

    class Meta:
        verbose_name_plural = "Recipies"