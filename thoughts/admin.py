from django.contrib import admin

from thoughts.models import Thought
from thoughts.models import ThoughtAssignment

class ThoughtAdmin(admin.ModelAdmin):
  fieldsets = [
      ('Detail', {'fields': ['text', 'user']}),
      ('Status', {'fields': ['is_locked']}),
  ]

  list_display = ('__unicode__', 'user', 'date_created','is_locked')
  list_filter = ('date_created', 'user', 'is_locked')

admin.site.register(Thought, ThoughtAdmin)
admin.site.register(ThoughtAssignment)
