# Generated by Django 5.0.3 on 2024-03-14 12:07

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Main', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='OnlineClass',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='Class Name')),
                ('price', models.FloatField(verbose_name='Price')),
                ('language', models.CharField(choices=[('Frensh', 'Frensh'), ('English', 'English')], max_length=10, verbose_name='Language')),
                ('zoom_link', models.CharField(max_length=255, verbose_name='Zoom Link')),
                ('classroom_link', models.CharField(max_length=255, verbose_name='Classroom Link')),
                ('updated', models.DateTimeField(auto_now=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Main.course')),
                ('students', models.ManyToManyField(blank=True, to='Main.student')),
                ('teacher', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Main.teacher')),
            ],
            options={
                'verbose_name': 'Online Class',
                'verbose_name_plural': 'Online Classes',
                'db_table': 'Online_Class',
                'ordering': ['-created'],
            },
        ),
        migrations.CreateModel(
            name='OnlineMessage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.TextField(blank=True, null=True, verbose_name='Body')),
                ('voice', models.FileField(blank=True, null=True, upload_to='voice/%y/%m/%d', verbose_name='Voice')),
                ('image', models.ImageField(blank=True, null=True, upload_to='image/%y/%m/%d', verbose_name='Image')),
                ('updated', models.DateTimeField(auto_now=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('onlineclass', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Online.onlineclass')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Online Message',
                'verbose_name_plural': 'Online Messages',
                'db_table': 'Online_Message',
                'ordering': ['created'],
            },
        ),
        migrations.CreateModel(
            name='OnlineOffer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60, verbose_name='Name')),
                ('price', models.FloatField(verbose_name='Price')),
                ('updated', models.DateTimeField(auto_now=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('onlineclasses', models.ManyToManyField(blank=True, to='Online.onlineclass')),
            ],
            options={
                'verbose_name': 'Online Offer',
                'verbose_name_plural': 'Online Offers',
                'db_table': 'Online_Offer',
                'ordering': ['-created'],
            },
        ),
        migrations.CreateModel(
            name='OnlineOfferRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('updated', models.DateTimeField(auto_now=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('onlineoffer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Online.onlineoffer')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Main.student')),
            ],
            options={
                'verbose_name': 'Online Offer Request',
                'verbose_name_plural': ' Online Offer Requests',
                'db_table': 'Online_Offer_Request',
                'ordering': ['-created'],
            },
        ),
        migrations.CreateModel(
            name='OnlineRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('updated', models.DateTimeField(auto_now=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('onlineclass', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Online.onlineclass')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Main.student')),
            ],
            options={
                'verbose_name': 'Online Request',
                'verbose_name_plural': ' Online Requests',
                'db_table': 'Online_Request',
                'ordering': ['-created'],
            },
        ),
    ]
