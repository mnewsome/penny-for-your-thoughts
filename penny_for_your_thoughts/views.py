from django.shortcuts import render

from thoughts.models import Thought
from thoughts.forms import ThoughtForm

def index(request):
  locked_thought_count = Thought.locked_thought_count()
  next_locked_thought = Thought.next_locked_thought()
  thought_form = get_thought_form(request)

  context = dict(
           locked_thought_count=locked_thought_count,
           next_locked_thought=next_locked_thought,
           thought_form=thought_form,
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
