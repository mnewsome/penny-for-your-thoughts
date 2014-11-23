from django.forms import ModelForm
from thoughts.models import Thought

class ThoughtForm(ModelForm):
  class Meta:
    model = Thought
    fields = ['text']
