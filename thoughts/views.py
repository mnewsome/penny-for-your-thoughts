from django.shortcuts import render

from thoughts.models import Thought

def show(request, thought_id):
   context = dict(
           thought = Thought.objects.get(pk=thought_id),
           )

   return render(request, 'thoughts/show.html', context)
