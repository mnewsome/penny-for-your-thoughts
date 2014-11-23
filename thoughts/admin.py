from django.contrib import admin
from thoughts.models import Thought

class ThoughtAdmin(admin.ModelAdmin):
  fieldsets = [
      ('Detail', {'fields': ['text']}),
      ('Status', {'fields': ['is_locked']}),
  ]

  list_filter = ('date_created',)

admin.site.register(Thought, ThoughtAdmin)
