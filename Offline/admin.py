from django.contrib import admin
from .models import OfflineClass, OfflineRequest, OfflineMessage
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from Main.models import Student


# Register your models here.
class OfflineClassInline(admin.TabularInline):
    model = OfflineClass
    extra = 0
    readonly_fields = ['name', 'course', 'classroom_link']
    fields = ['name', 'course', 'classroom_link']

    def has_delete_permission(self, request, obj=None):
        return False

    def has_add_permission(self, request, obj=None):
        return False


class OfflineMessageInline(admin.TabularInline):
    model = OfflineMessage
    extra = 0
    readonly_fields = ['user', 'created']
    fields = ['user', 'created']

    def has_delete_permission(self, request, obj=None):
        return False

    def has_add_permission(self, request, obj=None):
        return False


class OfflineClassAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'course_name', 'teacher_name', 'language', 'classroom_link', 'price')
    search_fields = ('id', 'name')
    inlines = [OfflineMessageInline]
    filter_horizontal = ('students',)
    list_filter = ('language',)
    list_per_page = 20

    def teacher_name(self, obj):
        if obj.teacher is not None:
            return obj.teacher.name
        else:
            return 'No Teacher Assigned'

    teacher_name.short_description = 'Teacher'

    def course_name(self, obj):
        if obj.course is not None:
            return obj.course.name
        else:
            return 'No Course Assigned'

    course_name.short_description = 'Course'

    def sendNewClassEmail(self, request, queryset):
        # students = Student.objects.all()
        for obj in queryset:
            students = Student.objects.filter(major=obj.course.major, language=obj.language, year=obj.course.year)
            for student in students:
                if student.user.email is not None:
                    email = student.user.email
                    subject = "New Offline Class is Open - GoTop Academy"
                    message = render_to_string('emails/new_offlineclass_email.html', {
                        'student': student.name,
                        'price': obj.price,
                        'teacher': obj.teacher.name,
                        'className': obj.name,
                        'courseName': obj.course.name,
                    })
                    email = EmailMessage(subject=subject, body=message, to=[email])
                    email.send()

    sendNewClassEmail.short_description = 'Send Notification Email For New Class'

    def deleteAllMessage(self, request, queryset):
        for obj in queryset:
            offlineclass = OfflineClass.objects.get(id=obj.id)
            OfflineMessage.objects.filter(offlineclass=offlineclass).delete()

    deleteAllMessage.short_description = 'Delete All Messages'

    actions = [sendNewClassEmail, deleteAllMessage]


class OfflineRequestAdmin(admin.ModelAdmin):
    list_display = ('id', 'student_id', 'student_name', 'offlineclass_id', 'offlineclass_name', 'created')

    def student_name(self, obj):
        return obj.student.name

    student_name.short_description = 'Student Name'

    def student_id(self, obj):
        return obj.student.id

    student_id.short_description = 'Student ID'

    def offlineclass_name(self, obj):
        return obj.offlineclass.name

    offlineclass_name.short_description = 'Class Name'

    def offlineclass_id(self, obj):
        return obj.offlineclass.id

    offlineclass_id.short_description = 'Class ID'

    def acceptStudent(self, request, queryset):
        for obj in queryset:
            offlineclass = OfflineClass.objects.get(id=obj.offlineclass.id)
            offlineclass.students.add(obj.student)
            offlineclass.save()
            email = obj.student.user.email
            subject = "Congratulations! You've Been Accepted into the " + obj.offlineclass.name
            message = render_to_string('emails/accept_request_email.html', {
                'student': obj.student.name,
                'className': obj.offlineclass.name,
                'courseName': obj.offlineclass.course.name,
            })
            email = EmailMessage(subject=subject, body=message, to=[email])
            email.send()
            obj.delete()

    acceptStudent.short_description = 'Accept Student'
    actions = [acceptStudent]


class OfflineMessageAdmin(admin.ModelAdmin):
    list_display = ('id', 'user_username', 'offlineclass_name', 'body', 'created')
    list_per_page = 20

    def user_username(self, obj):
        return obj.user.username

    user_username.short_description = 'Username'

    def offlineclass_name(self, obj):
        return obj.offlineclass.name

    offlineclass_name.short_description = 'Class'


admin.site.register(OfflineClass, OfflineClassAdmin)
admin.site.register(OfflineRequest, OfflineRequestAdmin)
admin.site.register(OfflineMessage, OfflineMessageAdmin)
