from django.template import Template, Context
from django.test import TestCase

class TestPaymentTags(TestCase):
  TEMPLATE = Template('{% load payment_tags %}{{donation_amount|currency}}')

  def test_total_donation_amount_is_formatted_properly(self):
    rendered_template = self.TEMPLATE.render(Context({ 'donation_amount':100 }))
    self.assertEqual('$100', str(rendered_template))
