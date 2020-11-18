import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "learning_log.settings")
#name of the project, not name of the app

import django
django.setup()

from learning_logs.models import Topic

topics = Topic.objects.all() #give me all the objects from the Topic model 

for topic in topics: #iterate through all objects
    print("Topic ID:", topic.id, " Topic:", topic)
    #topic.id is a sql attribute it automatically gives
    #why can we give it topic for the text instead of topic.text?
    #we defined a string method in an object, so it returns (self.text)
    #if we did not have that string method, it would return back garbage
    #if you have any string method, it is returning itself when you call for topic. 
    #topic essentially is topic.text 

t = Topic.objects.get(id=1) #we want to examine any attributes the object has
print(t.text) #text of the topic, the name
print(t.date_added)

entries = t.entry_set.all() #we can do this because we have defined a relationship between entry and topic by a foreign key
                            #the way we can access entries related to a certain topic is through a foreign key
                            #the topic has to be lower case

for entry in entries:
    print(entry) 