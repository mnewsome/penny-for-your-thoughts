from django.shortcuts               import render
from django.contrib.auth.models     import User
from django.contrib.auth.decorators import login_required

from thoughts.models import Thought

@login_required
def index(request):
	user = User.objects.get(username=request.user.username)
	thoughts = Thought.objects.filter(user=user)
	context = dict(
		general_user = user.generaluser,
		thoughts     = thoughts,
	)
	return render(request, 'accounts/index.html', context)
