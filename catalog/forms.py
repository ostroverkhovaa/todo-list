from django import forms
from django.forms import DateTimeInput

from catalog.models import Task, Tag


class TaskForm(forms.ModelForm):
    tags = forms.ModelMultipleChoiceField(
        queryset=Tag.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False,
    )

    class Meta:
        model = Task
        fields = ["content", "deadline", "tags"]
        labels = {
            "content": "Task content",
            "deadline": "Task deadline",
        }
        widgets = {
            "deadline": DateTimeInput(
                attrs={
                    "type": "datetime-local",
                },
                format="%Y-%m-%dT%H:%M"
            ),
        }
