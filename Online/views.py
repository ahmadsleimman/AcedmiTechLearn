from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import OnlineClass, OnlineOffer, OnlineRequest, OnlineOfferRequest, OnlineMessage
from Main.models import Student, Teacher

# Create your views here.


def Online(request):
    onlineclasses = OnlineClass.objects.all()
    onlineoffers = OnlineOffer.objects.all()

    context = {
        "onlineclasses": onlineclasses,
        "onlineoffers": onlineoffers,
    }

    return render(request, 'online.html', context)


@login_required(login_url='Login')
def OnlineDetails(request, id):
    try:
        onlineclass = OnlineClass.objects.get(id=id)
    except:
        return redirect("NotFound")

    onlinemessages = OnlineMessage.objects.filter(onlineclass=onlineclass)

    context = {
        "onlineclass": onlineclass,
        "onlinemessages": onlinemessages,
    }

    if hasattr(request.user, 'student'):
        isEnrolled = None
        student = Student.objects.get(user=request.user)

        if student in onlineclass.students.all():
            isEnrolled = True

        try:
            onlinerequest = OnlineRequest.objects.get(student=student, onlineclass=onlineclass)
            isRequested = True
        except:
            isRequested = False

        context.update({"isEnrolled": isEnrolled})
        context.update({"isRequested": isRequested})

    if hasattr(request.user, 'teacher'):
        isAdmin = None
        teacher = Teacher.objects.get(user=request.user)

        if teacher == onlineclass.teacher:
            isAdmin = True

        context.update({"isAdmin": isAdmin})

    return render(request, 'online-details.html', context)


@login_required(login_url='Login')
def OnlineEnroll(request, id):
    try:
        onlineclass = OnlineClass.objects.get(id=id)
    except:
        return redirect("NotFound")

    if hasattr(request.user, 'student'):
        studentID = Student.objects.get(user=request.user)
        onlinerequest = OnlineRequest.objects.create(student=studentID, onlineclass=onlineclass)
        onlinerequest.save()
    return redirect("OnlineDetails", id=id)


@login_required(login_url='Login')
def OnlineOfferDetails(request, id):
    try:
        onlineoffer = OnlineOffer.objects.get(id=id)
    except:
        return redirect("NotFound")

    context = {
        "onlineoffer": onlineoffer,
    }

    if hasattr(request.user, 'student'):
        student = Student.objects.get(user=request.user)

        try:
            onlineofferrequest = OnlineOfferRequest.objects.get(student=student)
            isRequested = True
        except:
            isRequested = False

        context.update({"isRequested": isRequested})

    return render(request, 'online-offer.html', context)


@login_required(login_url='Login')
def OnlineOfferEnroll(request, id):
    try:
        onlineoffer = OnlineOffer.objects.get(id=id)
    except:
        return redirect("NotFound")

    if hasattr(request.user, 'student'):
        studentID = Student.objects.get(user=request.user)
        onlineofferrequest = OnlineOfferRequest.objects.create(student=studentID, onlineoffer=onlineoffer)
        onlineofferrequest.save()
    return redirect("OnlineOffer", id=id)
