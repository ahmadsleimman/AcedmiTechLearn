from django.db import models
from django.contrib.auth.models import User
from Main.models import Student, Teacher, Course


# Create your models here.


class OfflineClass(models.Model):
    LANGUAGE = (
        ('Frensh', 'Frensh'),
        ('English', 'English'),
    )
    name = models.CharField(max_length=30, verbose_name='Class Name')
    teacher = models.ForeignKey(Teacher, on_delete=models.SET_NULL, null=True)
    price = models.FloatField(verbose_name='Price')
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    language = models.CharField(choices=LANGUAGE, max_length=10, verbose_name='Language')
    students = models.ManyToManyField(Student, blank=True)
    classroom_link = models.CharField(max_length=255, verbose_name='Classroom Link')
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.id} - {self.name}-{self.language}"

    class Meta:
        ordering = ['-created']
        verbose_name = "Offline Class"
        verbose_name_plural = "Offline Classes"
        db_table = 'Offline_Class'


class OfflineRequest(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    offlineclass = models.ForeignKey(OfflineClass, on_delete=models.CASCADE)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created']
        verbose_name = "Offline Request"
        verbose_name_plural = " Offline Requests"
        db_table = 'Offline_Request'

    def __str__(self):
        return f"{self.id}"


class OfflineMessage(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    offlineclass = models.ForeignKey(OfflineClass, on_delete=models.CASCADE)
    body = models.TextField(verbose_name='Body', null=True, blank=True)
    voice = models.FileField(verbose_name="Voice", upload_to="voice/%y/%m/%d", null=True, blank=True)
    image = models.ImageField(verbose_name="Image", upload_to="image/%y/%m/%d", null=True, blank=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created']
        verbose_name = "Offline Message"
        verbose_name_plural = "Offline Messages"
        db_table = 'Offline_Message'

    def __str__(self):
        return f"{self.id}"
