from django.shortcuts import render

from thoughts.models import Thought

def index(request):
  thoughts = Thought.objects.all().order_by('date_created')
  context = {'thoughts': thoughts}
  return render(request, 'thoughts/index.html', context)
