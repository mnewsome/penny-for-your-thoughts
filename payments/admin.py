from django.contrib import admin

from payments.models import Payment

class PaymentAdmin(admin.ModelAdmin):
  list_display = ('__unicode__', 'user', 'date_created', 'date_updated')
  list_filter = ('user', 'date_created', 'date_updated')

admin.site.register(Payment, PaymentAdmin)
