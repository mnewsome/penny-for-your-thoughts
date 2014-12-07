from django.shortcuts import render

from thoughts.forms import ThoughtForm
from thoughts.models import Thought
from thoughts.tasks import add

def index(request):
  context = dict(
           locked_thought_count=Thought.locked_thought_count(),
           unlocked_thought_count=Thought.unlocked_thought_count(),
           next_locked_thought=Thought.next_locked_thought(),
           thought_form=get_thought_form(request),
           )

  return render(request, 'index.html', context)

def get_thought_form(request):
  if request.method == 'POST':
    thought_form = ThoughtForm(request.POST)
    if thought_form.is_valid():
      thought_form.save()
  else:
    thought_form = ThoughtForm(initial={'user': request.user})

  return thought_form
