from django.contrib import admin

from catalog.models import Task, Tag


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    search_fields = ["content"]
    list_filter = ["is_done", "tags"]


admin.site.register(Tag)
