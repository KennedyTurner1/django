from django.shortcuts import render

# Create your views here.

#get some help on these

def index(request): #the first argument is always a request for a view because they want information
    #we want to replace the django homepage (rocket) with our homepage
    return render(request, 'learning_logs/index.html')

def topics(request):
    return render(request, 'learning_logs/topics.html')