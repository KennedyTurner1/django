from django.db import models
from django.contrib.auth.models import User

# Create your models here.
# Think of models as tables, and the attributes are text and date added. 
# models are kind of like your database

class Topic(models.Model):
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    #two attributes, text and date_added 
    owner = models.ForeignKey(User, on_delete=models.CASCADE) #User is a django model
    #we want to associate topics with each user 
    
    def __str__(self): #string method returns something useful instead of garbage
        return self.text 

class Entry(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True) #display the current time 
    
    class Meta:
        verbose_name_plural = 'entries' #the plural of entry is entries

    def __str__(self):
        return f"{self.text[:50]}..." #returns the entry with only the first 50 characters
