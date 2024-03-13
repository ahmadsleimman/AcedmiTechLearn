from django.shortcuts import render


# Create your views here.

def Home(request):
    return render(request, 'home.html')


def About(request):
    return render(request, 'about.html')


def Service(request):
    return render(request, 'service.html')


def ContactUs(request):
    # if request.method == 'POST':
    #     name = request.POST['name']
    #     email = request.POST['email']
    #     subject = request.POST['subject']
    #     message = request.POST['message']
    #     inbox = Inbox.objects.create(name=name, email=email, subject=subject, message=message)
    #     inbox.save()
    return render(request, 'contact-us.html')

def NotFound(request):
    return render(request, '404.html')