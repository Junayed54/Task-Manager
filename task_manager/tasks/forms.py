from django import forms
from .models import Task

class TaskCreateForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'priority', 'completed', 'image']

    # Add CSS classes to form fields
    def __init__(self, *args, **kwargs):
        super(TaskCreateForm, self).__init__(*args, **kwargs)
        self.fields['title'].widget.attrs.update({'class': 'form-control'})
        self.fields['description'].widget.attrs.update({'class': 'form-control', 'rows': '4'})
        self.fields['priority'].widget.attrs.update({'class': 'form-control'})
        # self.fields['completed'].widget.attrs.update({'class': 'form-check-input'})
        self.fields['image'].widget.attrs.update({'class': 'form-control-file'})
