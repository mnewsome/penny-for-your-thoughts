from django.shortcuts import render

from django.contrib.auth.models     import User
from django.contrib.auth.decorators import login_required

@login_required
def index(request):
	user = User.objects.get(username=request.user.username)
	context = dict(
		general_user = user.generaluser
	)
	return render(request, 'accounts/index.html', context)
