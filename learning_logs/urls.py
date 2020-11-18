from django.urls import path 

from .import views #importing views from our url file

app_name = 'learning_logs'

urlpatterns = [ #we are creating several urls
    path('',views.index, name='index'), #null because it is our home page, the name of the url is index
    path('topics',views.topics, name='topics'), #this is the topics url
    path('topics/<int:topic_id>/',views.topic, name='topic'), #topics_id comes from the database
    ]

