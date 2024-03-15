from django.shortcuts import render, redirect
from django.contrib import auth
from django.urls import reverse
from django.contrib.auth.models import User
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.contrib.sites.shortcuts import get_current_site
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.contrib.auth import get_user_model
from django.utils.encoding import force_bytes, force_str
from .models import Student, Teacher, Inbox

# Create your views here.

def Home(request):
    return render(request, 'home.html')


def About(request):
    return render(request, 'about.html')


def Service(request):
    return render(request, 'service.html')


def ContactUs(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']
        inbox = Inbox.objects.create(name=name, email=email, subject=subject, message=message)
        inbox.save()
    return render(request, 'contact-us.html')

def NotFound(request):
    return render(request, '404.html')

def loginUser(request):
    error_message = None

    if request.user.is_authenticated:
        return redirect('Home')

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user_auth = auth.authenticate(request, username=username, password=password)
        if user_auth is not None:
            user = User.objects.get(username=username)
            try:
                data = Student.objects.get(user=user)
                auth.login(request, user_auth)
                return redirect('Home')
            except:
                try:
                    data = Teacher.objects.get(user=user)
                    auth.login(request, user_auth)
                    return redirect('Home')
                except:
                    error_message = "Account Not Found"
                    return render(request, 'login.html', {'error_message': error_message})
        else:
            error_message = "Invalid Credentials"
            return render(request, 'login.html', {'error_message': error_message})
    return render(request, 'loginNew.html', {'error_message': error_message})


def registerUser(request):
    error_message = None

    if request.user.is_authenticated:
        return redirect('Home')

    if request.method == "POST":
        name = request.POST['fullname']
        major = request.POST['major']
        language = request.POST['language']
        year = request.POST['year']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirmpassword = request.POST['confirmpassword']

        if password != confirmpassword:
            error_message = "Password And Confirm Password Should Be The Same"
            return render(request, 'register.html', {'error_message': error_message})

        if year == '1':
            error_message = "Select A Specific Year"
            return render(request, 'register.html', {'error_message': error_message})

        if major == '1':
            error_message = "Select A Specific Major"
            return render(request, 'register.html', {'error_message': error_message})

        try:
            user = User.objects.get(username=username)
            error_message = "Username already exists!!"
            return render(request, 'register.html', {'error_message': error_message})
        except:
            try:
                user = User.objects.get(email=email)
                error_message = "Email already exists!!"
                return render(request, 'register.html', {'error_message': error_message})
            except:
                new_user = User.objects.create(username=username, email=email)
                new_user.set_password(password)
                new_user.is_active = False
                new_user.save()

                new_student = Student.objects.create(name=name, major=major, language=language, year=year,
                                                     user=new_user)
                new_student.save()

                current_site = get_current_site(request)
                uid = urlsafe_base64_encode(force_bytes(new_student.user.pk))
                token = default_token_generator.make_token(new_student.user)
                verification_url = reverse('verify_email', args=[uid, token])
                verification_link = f'http://{current_site.domain}{verification_url}'
                subject = "Verify Your Account"
                message = render_to_string('emails/verification_email.html', {
                    'student': new_student,
                    'verification_link': verification_link,
                })
                email = EmailMessage(subject=subject, body=message, to=[new_student.user.email])
                email.send()
                return render(request, 'verification_message.html')
    return render(request, 'registerNew.html', {'error_message': error_message})


def logout(request):
    auth.logout(request)
    return redirect('Home')


def verify_email(request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64).decode())
        User = get_user_model()
        user = User.objects.get(pk=uid)
        if default_token_generator.check_token(user, token):
            user.is_active = True
            user.save()
            return redirect('Login')
        else:
            return redirect('NotFound')
    except User.DoesNotExist:
        return redirect('NotFound')