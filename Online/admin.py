from django.contrib import admin
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from .models import OnlineClass, OnlineRequest, OnlineMessage, OnlineFinancialAid
from Main.models import Student


# Register your models here.

class OnlineClassInline(admin.TabularInline):
    model = OnlineClass
    extra = 0
    readonly_fields = ['name', 'course', 'classroom_link', 'zoom_link']
    fields = ['name', 'course', 'classroom_link', 'zoom_link']

    def has_delete_permission(self, request, obj=None):
        return False

    def has_add_permission(self, request, obj=None):
        return False


class OnlineMessageInline(admin.TabularInline):
    model = OnlineMessage
    extra = 0
    readonly_fields = ['user', 'created']
    fields = ['user', 'created']

    def has_delete_permission(self, request, obj=None):
        return False

    def has_add_permission(self, request, obj=None):
        return False


class OnlineClassAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'course_name', 'teacher_name', 'language', 'zoom_link', 'classroom_link', 'price')
    search_fields = ('id', 'name')
    inlines = [OnlineMessageInline]
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
                    subject = "New Online Class is Open - GoTop Academy"
                    message = render_to_string('emails/new_onlineclass_email.html', {
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
            onlineclass = OnlineClass.objects.get(id=obj.id)
            OnlineMessage.objects.filter(onlineclass=onlineclass).delete()

    deleteAllMessage.short_description = 'Delete All Messages'

    actions = [sendNewClassEmail, deleteAllMessage]


class OnlineRequestAdmin(admin.ModelAdmin):
    list_display = ('id', 'student_id', 'student_name', 'onlineclass_id', 'onlineclass_name', 'created')

    def student_name(self, obj):
        return obj.student.name

    student_name.short_description = 'Student Name'

    def student_id(self, obj):
        return obj.student.id

    student_id.short_description = 'Student ID'

    def onlineclass_name(self, obj):
        return obj.onlineclass.name

    onlineclass_name.short_description = 'Class Name'

    def onlineclass_id(self, obj):
        return obj.onlineclass.id

    onlineclass_id.short_description = 'Class ID'

    def acceptStudent(self, request, queryset):
        for obj in queryset:
            onlineclass = OnlineClass.objects.get(id=obj.onlineclass.id)
            onlineclass.students.add(obj.student)
            onlineclass.save()
            email = obj.student.user.email
            subject = "Congratulations! You've Been Accepted into the " + obj.onlineclass.name
            message = render_to_string('emails/accept_request_email.html', {
                'student': obj.student.name,
                'className': obj.onlineclass.name,
                'courseName': obj.onlineclass.course.name,
            })
            email = EmailMessage(subject=subject, body=message, to=[email])
            email.send()
            obj.delete()

    acceptStudent.short_description = 'Accept Student'
    actions = [acceptStudent]


class OnlineMessageAdmin(admin.ModelAdmin):
    list_display = ('id', 'user_username', 'onlineclass_name', 'body', 'created')
    list_per_page = 20

    def user_username(self, obj):
        return obj.user.username

    user_username.short_description = 'Username'

    def onlineclass_name(self, obj):
        return obj.onlineclass.name

    onlineclass_name.short_description = 'Class'


class OnlineFinancialAidAdmin(admin.ModelAdmin):
    list_display = ('id', 'student_id', 'student_name', 'onlineclass_id', 'onlineclass_name', 'message', 'created')
    list_per_page = 5

    def student_name(self, obj):
        return obj.student.name

    student_name.short_description = 'Student Name'

    def student_id(self, obj):
        return obj.student.id

    student_id.short_description = 'Student ID'

    def onlineclass_name(self, obj):
        return obj.onlineclass.name

    onlineclass_name.short_description = 'Class Name'

    def onlineclass_id(self, obj):
        return obj.onlineclass.id

    onlineclass_id.short_description = 'Class ID'


admin.site.register(OnlineClass, OnlineClassAdmin)
admin.site.register(OnlineRequest, OnlineRequestAdmin)
admin.site.register(OnlineMessage, OnlineMessageAdmin)
admin.site.register(OnlineFinancialAid, OnlineFinancialAidAdmin)
