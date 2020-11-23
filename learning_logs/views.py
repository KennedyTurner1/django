from django.shortcuts import render, redirect 
from .models import Topic, Entry #have to import the model to have access to the model
from .forms import TopicForm, EntryForm

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

def new_topic(request):
    if request.method != 'POST': #if it is a get method
        form = TopicForm()
    else:
        form = TopicForm(data=request.POST)

        if form.is_valid():
            form.save() #this is what the view will use to take what is on the form and put it on the database

            #redirect the user to the topics page when they have used a submit button 
            return redirect('learning_logs:topics')

    context = {'form':form}

    return render(request, 'learning_logs/new_topic.html', context)

def new_entry(request, topic_id):
    topic = Topic.objects.get(id=topic_id)
    if request.method != 'POST': #if it is a get method
        form = EntryForm() #creates just a blank form not associated to any entry
    else:
        form = EntryForm(data=request.POST)

        if form.is_valid():
            
            new_entry = form.save(commit=False) #this is what the view will use to take what is on the form and put it on the database
            new_entry.topic = topic 
            new_entry.save()
            form.save()
            #redirect the user to the topics page when they have used a submit button 
            return redirect('learning_logs:topic', topic_id=topic_id)

    context = {'form':form, 'topic':topic}
 
    return render(request, 'learning_logs/new_entry.html', context)

def edit_entry(request, entry_id):
    entry = Entry.objects.get(id=entry_id) #this is an instance of the model Entry
    topic = entry.topic #we have defined the topic that we are using

    if request.method != 'POST': #we want to edit an existing entry
        form = EntryForm(instance=entry) #instance belongs to the entry we just created
    else: #if not a post request but a get request
        form = EntryForm(instance=entry, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('learning_logs:topic', topic_id=topic.id) #after they have clicked save, then they will be redirected to where

    context = {'entry':entry, 'topic':topic, 'form':form} #the context is the context given to the skeleton
    return render(request, 'learning_logs/edit_entry.html', context) #the template is a skeleton, but it doesnt have the content


