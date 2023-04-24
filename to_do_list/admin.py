from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group

from to_do_list.models import Tag, Task, Person

admin.site.unregister(Group)


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ["name"]


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = [
        "owner",
        "description",
        "deadline",
        "is_completed",
     ]
    list_filter = [
        "deadline",
        "is_completed",
    ]
    search_fields = [
        "owner",
    ]


@admin.register(Person)
class PersonAdmin(UserAdmin):
    list_display = UserAdmin.list_display
