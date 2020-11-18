from django.shortcuts import render
from .models import Topic  

# Create your views here.

#get some help on these

def index(request): #the first argument is always a request for a view because they want information
    #we want to replace the django homepage (rocket) with our homepage
    return render(request, 'learning_logs/index.html')

#to get all topics
def topics(request): #this is the topics view, the view is the go between for the html template and the database
    #brings in an object from the models file, which is the database, and saves it as a list of objects
    topics = Topic.objects.order_by('date_added') #order_by is the sort

    context = {'topics':topics} #template tag topics

    return render(request, 'learning_logs/topics.html', context) #this is what we return 
    #app is called learning_logs, and it will look for a file called topics.html in that folder
    #and then add the topics to the dictionary in that file
    #two types of requests, get requests and post requests
    #it will call the html page and then go to the topics html, and it will display it on the userface

#to get individual topics
def topic(request, topic_id): #this is where that variable comes into play
    topic = Topic.objects.get(id=topic_id)
    entries = topic.entry_set.order_by('-date_added')

    context = {'topic':topic, 'entries':entries}
    return render(request, 'learning_logs/topic.html', context)