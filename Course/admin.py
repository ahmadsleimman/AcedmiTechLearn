from django.contrib import admin
from .models import Course, Class, ClassRequest, CLassMessage, ClassFinancialAid


# Register your models here.

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'major', 'year', 'semester')
    search_fields = ('id', 'name')
    list_filter = ('major', 'year', 'semester')
    list_per_page = 20
