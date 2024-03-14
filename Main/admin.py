from django.contrib import admin
from .models import Student, Course, Teacher, Inbox
from Online.admin import OnlineClassInline
from Offline.admin import OfflineClassInline
from VIP.admin import VIPClassInline

# Register your models here.

class StudentAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'username', 'major', 'language', 'year')
    search_fields = ('id', 'name')
    list_filter = ('major', 'language', 'year')
    list_per_page = 20

    def email(self, obj):
        return obj.user.email

    email.short_description = 'email'

    def username(self, obj):
        return obj.user.username

    username.short_description = 'username'


class TeacherAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'username')
    search_fields = ('id', 'name')
    inlines = [OfflineClassInline, OnlineClassInline, VIPClassInline]

    def email(self, obj):
        return obj.user.email

    email.short_description = 'email'

    def username(self, obj):
        return obj.user.username

    username.short_description = 'username'


class CourseAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'major', 'year', 'semester')
    search_fields = ('id', 'name')
    list_filter = ('major', 'year', 'semester')
    list_per_page = 20


class InboxAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'subject', 'message', 'created', 'isFeedback')
    search_fields = ('id', 'name', 'subject')
    list_filter = ('isFeedback',)
    list_per_page = 20


admin.site.register(Student, StudentAdmin)
admin.site.register(Teacher, TeacherAdmin)
admin.site.register(Course, CourseAdmin)
admin.site.register(Inbox, InboxAdmin)
