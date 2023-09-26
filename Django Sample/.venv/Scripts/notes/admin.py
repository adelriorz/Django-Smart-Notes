from django.contrib import admin

from . import models

class NotesAdmin(admin.ModelAdmin):
    list_display = ('title',)

# This model is attached to this admin model to link via view
admin.site.register(models.Notes, NotesAdmin)