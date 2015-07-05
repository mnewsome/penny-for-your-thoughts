from django.shortcuts import redirect
from django.views.decorators.http import require_POST

from lib.payment_manager import PaymentManager
from payments.interactor import Interactor

@require_POST
def charge(request):
    interactor = Interactor(PaymentManager())
    interactor.charge(request)
    return redirect('penny_for_your_thoughts.views.index')
