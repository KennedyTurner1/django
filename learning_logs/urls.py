from django.urls import path 
from .import views #importing views from our url file

app_name = 'learning_logs'

urlpatterns = [ #we are creating several urls
    path('',views.index, name='index'), #null because it is our home page, the name of the url is index
    path('topics',views.topics, name='topics'), #this is the topics url
    path('topics/<int:topic_id>/',views.topic, name='topic'), #topics_id comes from the database
    path('new_topic/', views.new_topic, name='new_topic'),
    path('new_entry/<int:topic_id>/', views.new_entry, name='new_entry'), #topic id for new entry because we want it to be associated with the topic
    path('edit_entry/<int:entry_id>/', views.edit_entry, name='edit_entry'), #pull the entry id to edit the right one
    ]

#urls, view, html template
#get is to read data from the data base
#post is to send data from the data base 
