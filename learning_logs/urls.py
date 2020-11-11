from django.urls import path 

from .import views #importing views from our url file

app_name = 'learning_logs'

urlpatterns = [ #we are creating several urls
    path('',views.index, name='index') #null because it is our home page, the name of the url is index
    path('',views.topics, name='topics')
]

