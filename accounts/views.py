from django.db.models               import Sum
from django.contrib.auth.models     import User
from django.contrib.auth.decorators import login_required
from django.shortcuts               import render

from thoughts.models import Thought
from payments.models import Payment

@login_required
def index(request):
	user = User.objects.get(username=request.user.username)
	thoughts = Thought.objects.filter(user=user)

	context = dict(
		general_user    = user.generaluser,
		thoughts        = thoughts,
		donation_amount = donation_amount(user),
	)
	return render(request, 'accounts/index.html', context)

def donation_amount(user):
	payments = Payment.objects.filter(user=user).aggregate(Sum('amount'))
	return int(payments['amount__sum'] * .01)
