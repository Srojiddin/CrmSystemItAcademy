from django.contrib import admin

from apps.students.models import Student

admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['full_name']
    exclude = [
        'groups',
        'first_name',
        'last_name',
        'user_permissions',
    ]

admin.site.register(Student)