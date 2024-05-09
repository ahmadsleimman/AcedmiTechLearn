from django.contrib import admin
from .models import Student, Teacher, Inbox
from Course.admin import ClassInline
from import_export.admin import ImportExportModelAdmin
from .resource import StudentResource, TeacherResource, InboxResource
from admincharts.admin import AdminChartMixin
from django.db.models import Count


# Register your models here.


@admin.register(Student)
class StudentAdmin(AdminChartMixin, ImportExportModelAdmin):
    list_display = ('id', 'name', 'email', 'username', 'track', 'created')
    search_fields = ('id', 'name')
    list_filter = ('track',)
    list_per_page = 30
    resource_class = StudentResource

    def get_list_chart_data(self, queryset):
        track_counts = Student.objects.values('track').annotate(count=Count('id'))
        labels = [track['track'] for track in track_counts]
        data = [track['count'] for track in track_counts]
        colors = ['rgba(255, 99, 132, 0.7)', 'rgba(54, 162, 235, 0.7)', 'rgba(255, 206, 86, 0.7)',
                  'rgba(75, 192, 192, 0.7)', 'rgba(153, 102, 255, 0.7)', 'rgba(255, 159, 64, 0.7)',
                  'rgba(255, 99, 132, 0.7)']
        # Return chart data
        return {
            "labels": labels,
            "datasets": [
                {
                    "label": "Number of Students",
                    "data": data,
                    "backgroundColor": colors[:len(labels)],
                }
            ]
        }

    @admin.display(description="Email", ordering="user__email")
    def email(self, obj):
        return obj.user.email

    @admin.display(description="Username", ordering="user__username")
    def username(self, obj):
        return obj.user.username

    def has_import_permission(self, request):
        return False

    def has_export_permission(self, request):
        # Only superusers have export permission
        return request.user.is_superuser


@admin.register(Teacher)
class TeacherAdmin(ImportExportModelAdmin):
    list_display = ('id', 'name', 'email', 'username', 'created')
    search_fields = ('id', 'name')
    inlines = [ClassInline]
    resource_class = TeacherResource

    @admin.display(description="Email", ordering="user__email")
    def email(self, obj):
        return obj.user.email

    @admin.display(description="Username", ordering="user__username")
    def username(self, obj):
        return obj.user.username

    def has_import_permission(self, request):
        return False

    def has_export_permission(self, request):
        # Only superusers have export permission
        return request.user.is_superuser


@admin.register(Inbox)
class InboxAdmin(ImportExportModelAdmin):
    list_display = ('id', 'name', 'email', 'subject', 'message', 'isFeedback', 'created')
    search_fields = ('id', 'name', 'subject', 'email')
    list_filter = ('isFeedback',)
    list_per_page = 20
    resource_class = InboxResource

    def has_import_permission(self, request):
        return False

    def has_export_permission(self, request):
        # Only superusers have export permission
        return request.user.is_superuser
