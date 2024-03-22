from django.db import models
from django.contrib.auth.models import User

class blog(models.Model):
    name = models.CharField(max_length=30, unique=True)
    description = models.CharField(max_length=100)
    
class Topic(models.Model):
    subject = models.CharField(max_length=255)
    last_updated = models.DateTimeField(auto_now_add=True)
    blog = models.ForeignKey(blog, on_delete=models.DO_NOTHING,related_name='topics')
    starter = models.ForeignKey(User,on_delete=models.DO_NOTHING, related_name='topics')

class Post(models.Model):
    message = models.TextField(max_length=4000)
    topic = models.ForeignKey(Topic,on_delete=models.DO_NOTHING, related_name='posts')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(null=True)
    created_by = models.ForeignKey(User,on_delete=models.DO_NOTHING, related_name='posts')
    updated_by = models.ForeignKey(User, on_delete=models.DO_NOTHING,null=True, related_name='+')




# Create your models here.
