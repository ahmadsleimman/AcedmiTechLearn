from django.contrib import admin
from .models import Student, Teacher, Inbox
from Course.admin import ClassInline


# Register your models here.


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'username', 'track', 'created')
    search_fields = ('id', 'name')
    list_filter = ('track',)
    list_per_page = 30

    @admin.display(description="Email", ordering="user__email")
    def email(self, obj):
        return obj.user.email

    @admin.display(description="Username", ordering="user__username")
    def username(self, obj):
        return obj.user.username


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'username', 'created')
    search_fields = ('id', 'name')
    inlines = [ClassInline]

    @admin.display(description="Email", ordering="user__email")
    def email(self, obj):
        return obj.user.email

    @admin.display(description="Username", ordering="user__username")
    def username(self, obj):
        return obj.user.username


@admin.register(Inbox)
class InboxAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'subject', 'message', 'isFeedback', 'created')
    search_fields = ('id', 'name', 'subject', 'email')
    list_filter = ('isFeedback',)
    list_per_page = 20
