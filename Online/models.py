from django.db import models
from django.contrib.auth.models import User
from Main.models import Student, Teacher, Course


# Create your models here.


class OnlineClass(models.Model):
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
    zoom_link = models.CharField(max_length=255, verbose_name='Zoom Link')
    classroom_link = models.CharField(max_length=255, verbose_name='Classroom Link')
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.id} - {self.name}-{self.language}"

    class Meta:
        ordering = ['-created']
        verbose_name = "Online Class"
        verbose_name_plural = "Online Classes"
        db_table = 'Online_Class'


class OnlineRequest(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    onlineclass = models.ForeignKey(OnlineClass, on_delete=models.CASCADE)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created']
        verbose_name = "Online Request"
        verbose_name_plural = " Online Requests"
        db_table = 'Online_Request'

    def __str__(self):
        return f"{self.id}"


class OnlineOffer(models.Model):
    name = models.CharField(max_length=60, verbose_name='Name')
    onlineclasses = models.ManyToManyField(OnlineClass, blank=True)
    price = models.FloatField(verbose_name='Price')
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created']
        verbose_name = "Online Offer"
        verbose_name_plural = "Online Offers"
        db_table = 'Online_Offer'

    def __str__(self):
        return self.name


class OnlineOfferRequest(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    onlineoffer = models.ForeignKey(OnlineOffer, on_delete=models.CASCADE)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created']
        verbose_name = "Online Offer Request"
        verbose_name_plural = " Online Offer Requests"
        db_table = 'Online_Offer_Request'

    def __str__(self):
        return f"{self.id}"


class OnlineMessage(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    onlineclass = models.ForeignKey(OnlineClass, on_delete=models.CASCADE)
    body = models.TextField(verbose_name='Body', null=True, blank=True)
    voice = models.FileField(verbose_name="Voice", upload_to="voice/%y/%m/%d", null=True, blank=True)
    image = models.ImageField(verbose_name="Image", upload_to="image/%y/%m/%d", null=True, blank=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created']
        verbose_name = "Online Message"
        verbose_name_plural = "Online Messages"
        db_table = 'Online_Message'

    def __str__(self):
        return f"{self.id}"
