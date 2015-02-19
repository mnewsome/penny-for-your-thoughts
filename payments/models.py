from django.db import models
from django.contrib.auth.models import User

class Payment(models.Model):
  user = models.ForeignKey(User)
  stripe_customer_id = models.CharField(max_length=100)
  amount = models.IntegerField(blank=False)
  date_created = models.DateTimeField(auto_now_add=True)
  date_updated = models.DateTimeField(auto_now=True)

  def __unicode__(self):
    return 'Payment ID:{}  Amount: {}  By: {}'.format(self.pk, self.amount, self.user)

  @classmethod
  def total_dollars_donated(cls):
    amount_in_cents = Payment.objects.aggregate(models.Sum('amount'))['amount__sum']
    return amount_in_cents / 100 if amount_in_cents is not None else 0
