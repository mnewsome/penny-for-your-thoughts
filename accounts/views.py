from django.contrib.auth.decorators import login_required
from django.shortcuts               import render

from accounts.interactor import Interactor

@login_required
def index(request):
	interactor = Interactor(request)
	return render(request, 'accounts/index.html', interactor.presenter())
