from django.contrib import admin
from . import models

# Register your models here.

class TaskAdmin(admin.ModelAdmin):
    list_display=('task', 'is_comp', 'updated_ts')
    search_fields=('task',)

admin.site.register(models.Task, TaskAdmin)