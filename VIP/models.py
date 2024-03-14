from django.db import models
from django.contrib.auth.models import User
from Main.models import Student, Teacher, Course


# Create your models here.


class VIPCourse(models.Model):
    LANGUAGE = (
        ('Frensh', 'Frensh'),
        ('English', 'English'),
    )
    name = models.CharField(max_length=30, verbose_name='VIP Name')
    teacher = models.ForeignKey(Teacher, on_delete=models.SET_NULL, null=True)
    price = models.FloatField(verbose_name='Price')
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    language = models.CharField(choices=LANGUAGE, max_length=10, verbose_name='Language')
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.id} - {self.name}-{self.language}"

    class Meta:
        ordering = ['-created']
        verbose_name = "VIP Course"
        verbose_name_plural = "VIP Courses"
        db_table = 'VIP_Course'


class VIPClass(models.Model):
    name = models.CharField(max_length=30, verbose_name='Class Name')
    vip_course = models.ForeignKey(VIPCourse, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.SET_NULL, null=True)
    teacher = models.ForeignKey(Teacher, on_delete=models.SET_NULL, null=True)
    zoom_link = models.CharField(max_length=255, verbose_name='Zoom Link')
    classroom_link = models.CharField(max_length=255, verbose_name='Classroom Link')
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.id} - {self.name}"

    class Meta:
        ordering = ['-created']
        verbose_name = "VIP Class"
        verbose_name_plural = "VIP Classes"
        db_table = 'VIP_Class'


class VIPRequest(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    vip_course = models.ForeignKey(VIPCourse, on_delete=models.CASCADE)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created']
        verbose_name = "VIP Request"
        verbose_name_plural = " VIP Requests"
        db_table = 'VIP_Request'

    def __str__(self):
        return f"{self.id}"


class VIPMessage(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    vipclass = models.ForeignKey(VIPClass, on_delete=models.CASCADE)
    body = models.TextField(verbose_name='Body', null=True, blank=True)
    voice = models.FileField(verbose_name="Voice", upload_to="voice/%y/%m/%d", null=True, blank=True)
    image = models.ImageField(verbose_name="Image", upload_to="image/%y/%m/%d", null=True, blank=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created']
        verbose_name = "VIP Message"
        verbose_name_plural = "VIP Messages"
        db_table = 'VIP_Message'

    def __str__(self):
        return f"{self.id}"
