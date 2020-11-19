from django import forms
from .models import Topic, Entry

class TopicForm(forms.ModelForm): #modelform uses the models already in your project
    class Meta:
        model = Topic
        fields = ['text']
        labels = {'text' : ''}

class EntryForm(forms.ModelForm):
    class Meta: #allows you to pull directly from the models.py file, already structured variables
        model = Entry
        fields = ['text']
        labels = {'text':''}

        widgets = {'text': forms.Textarea(attrs={'cols': 80})}
