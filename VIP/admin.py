from django.contrib import admin
from .models import VIPCourse, VIPClass, VIPRequest, VIPMessage
from Main.models import Student, Teacher


# Register your models here.

class VIPClassInline(admin.TabularInline):
    model = VIPClass
    extra = 0
    readonly_fields = ['name', 'vip_course', 'student']
    fields = ['name', 'vip_course', 'student']

    def has_delete_permission(self, request, obj=None):
        return False

    def has_add_permission(self, request, obj=None):
        return False


class VIPMessageInline(admin.TabularInline):
    model = VIPMessage
    extra = 0
    readonly_fields = ['user', 'created']
    fields = ['user', 'created']

    def has_delete_permission(self, request, obj=None):
        return False

    def has_add_permission(self, request, obj=None):
        return False


class VIPCourseAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'course_name', 'teacher_name', 'language', 'price')
    search_fields = ('id', 'name')
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


class VIPClassAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'name', 'vip_course_name', 'student_name', 'teacher_name', 'zoom_link', 'classroom_link', 'created')
    search_fields = ('id', 'name')
    list_per_page = 20
    inlines = [VIPMessageInline]

    def vip_course_name(self, obj):
        if obj.vip_course is not None:
            return obj.vip_course.name
        else:
            return 'No Class Assigned'

    vip_course_name.short_description = 'VIP CLass'

    def teacher_name(self, obj):
        if obj.teacher is not None:
            return obj.teacher.name
        else:
            return 'No Teacher Assigned'

    teacher_name.short_description = 'Teacher'

    def student_name(self, obj):
        if obj.student is not None:
            return obj.student.name
        else:
            return 'No Student Assigned'

    student_name.short_description = 'Student'

    def deleteAllMessage(self, request, queryset):
        for obj in queryset:
            vipclass = VIPClass.objects.get(id=obj.id)
            VIPMessage.objects.filter(vipclass=vipclass).delete()

    deleteAllMessage.short_description = 'Delete All Messages'

    actions = [deleteAllMessage]

    # filepath = obj.file.path
    # try:
    #     os.remove(filepath)
    #     obj.delete()
    # except:
    #     raise ValidationError("Can Not Delete The File")


class VIPRequestAdmin(admin.ModelAdmin):
    list_display = ('id', 'student_id', 'student_name', 'vipclass_id', 'vipclass_name', 'created')

    def student_name(self, obj):
        return obj.student.name

    student_name.short_description = 'Student Name'

    def student_id(self, obj):
        return obj.student.id

    student_id.short_description = 'Student ID'

    def vipclass_name(self, obj):
        return obj.vip_course.name

    vipclass_name.short_description = 'Course Name'

    def vipclass_id(self, obj):
        return obj.vip_course.id

    vipclass_id.short_description = 'Course ID'

    def acceptStudent(self, request, queryset):
        for obj in queryset:
            vip_course = VIPCourse.objects.get(id=obj.vip_course.id)
            student = Student.objects.get(id=obj.student.id)
            teacher = Teacher.objects.get(id=obj.vip_course.teacher.id)
            vip_class = VIPClass.objects.create(name=vip_course.name, vip_course=vip_course, student=student,
                                                teacher=teacher)
            vip_class.save()
            # email = obj.student.user.email
            # subject = "Congratulations! You've Been Accepted into the " + obj.offlineclass.name
            # message = render_to_string('emails/accept_request_email.html', {
            #     'student': obj.student.name,
            #     'className': obj.offlineclass.name,
            #     'courseName': obj.offlineclass.course.name,
            # })
            # email = EmailMessage(subject=subject, body=message, to=[email])
            # email.send()
            obj.delete()

    acceptStudent.short_description = 'Accept Student'
    actions = [acceptStudent]


class VIPMessageAdmin(admin.ModelAdmin):
    list_display = ('id', 'user_username', 'vip_class_id', 'vip_class_name', 'created')
    list_per_page = 20

    def user_username(self, obj):
        return obj.user.username

    user_username.short_description = 'Username'

    def vip_class_id(self, obj):
        return obj.vipclass.id

    vip_class_id.short_description = 'Class ID'

    def vip_class_name(self, obj):
        return obj.vipclass.name

    vip_class_name.short_description = 'Class Name'


admin.site.register(VIPCourse, VIPCourseAdmin)
admin.site.register(VIPClass, VIPClassAdmin)
admin.site.register(VIPRequest, VIPRequestAdmin)
admin.site.register(VIPMessage, VIPMessageAdmin)
