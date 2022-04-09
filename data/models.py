from django.db import models
from django.urls import reverse
import uuid

# Create your models here.
    
class Video(models.Model):
    upload = models.FileField(upload_to = 'videos/')
    title=models.CharField(max_length=100, null=False, blank=False)
    description=models.TextField(help_text="Video Description", null=True, blank=True)
    category=models.CharField(max_length=100, help_text="Enter Video Category", null=True, blank=False)
    date_created = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    
    def _str_(self):
        return self.title
        
    def get_absolute_url(self):
        return reverse('video_detail', args=[str(self.id)])
        
    def get_another_url(self):
        return reverse('video_detail_out', args=[str(self.id)])
      
    
    class Meta:
      db_table = "video"

class User(models.Model):
    username = models.CharField(max_length=50,null=False, blank=False,default="")
    email = models.CharField(max_length=50, default="")
    password = models.CharField(max_length = 100, default="", null=False, blank=False)
  
    
    def get_absolute_url(self):
        return reverse('upload_detail', args=[str(self.id)])
        
    def _str_(self):
        return self.username

class Question(models.Model):
    question = models.CharField(max_length = 300,null=False, blank=False)
    date_created = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    more_description = models.TextField(null=True, blank=True)
    
    class Meta:
        db_table = "question"
        
    def _str_(self):
        return self.question
    def get_absolute_url(self):
        return reverse('questions_url_in', args=[str(self.id)])
    def get_another_url(self):
        return reverse('questions_url_out', args=[str(self.id)])

class Comment(models.Model):
    user = models.ForeignKey('User', default='User', null=True, on_delete=models.SET_NULL)
    video = models.ForeignKey(Video,on_delete=models.CASCADE,related_name='comments', null=True, blank=True)
    question = models.ForeignKey(Question, default="admin", null=True, on_delete=models.SET_NULL)
    commenting = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)
    question = models.ForeignKey('Question',on_delete=models.CASCADE,null=True, blank=True)
    def _str_(self):
        return self.commenting
      
class Image(models.Model):
    title = models.CharField(max_length = 50, null=False, blank=False)
    picture = models.FileField(upload_to = 'pictures/')
    description=models.TextField(help_text="image Description", null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    
    def _str_(self):
        return self.title
    def get_absolute_url(self):
        return reverse('image_detail', args=[str(self.id)])
    class Meta:
        db_table = "image"
   
class Channel(models.Model):
    user = models.ForeignKey('User', default='User', null=True, on_delete=models.SET_NULL)
    avatar = models.FileField(default=1, upload_to='profile_images')
    def _str_(self):
        return self.channel.username
        
    def get_absolute_url(self):
        return reverse('channel-detail', args=[str(self.id)])