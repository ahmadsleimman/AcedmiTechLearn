from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import OfflineClass, OfflineOffer, OfflineRequest, OfflineOfferRequest, OfflineMessage
from Main.models import Student, Teacher

# Create your views here.

def Offline(request):
    offlineclasses = OfflineClass.objects.all()
    offlineoffers = OfflineOffer.objects.all()

    context = {
        "offlineclasses": offlineclasses,
        "offlineoffers": offlineoffers,
    }

    return render(request, 'offline.html', context)


@login_required(login_url='Login')
def OfflineDetails(request, id):
    try:
        offlineclass = OfflineClass.objects.get(id=id)
    except:
        return redirect("NotFound")

    offlinemessages = OfflineMessage.objects.filter(offlineclass=offlineclass)

    context = {
        "offlineclass": offlineclass,
        "offlinemessages": offlinemessages,
    }

    if hasattr(request.user, 'student'):
        isEnrolled = None
        student = Student.objects.get(user=request.user)

        if student in offlineclass.students.all():
            isEnrolled = True

        try:
            offlinerequest = OfflineRequest.objects.get(student=student, offlineclass=offlineclass)
            isRequested = True
        except:
            isRequested = False

        context.update({"isEnrolled": isEnrolled})
        context.update({"isRequested": isRequested})

    if hasattr(request.user, 'teacher'):
        isAdmin = None
        teacher = Teacher.objects.get(user=request.user)

        if teacher == offlineclass.teacher:
            isAdmin = True

        context.update({"isAdmin": isAdmin})

    return render(request, 'offline-details.html', context)


@login_required(login_url='Login')
def OfflineEnroll(request, id):
    try:
        offlineclass = OfflineClass.objects.get(id=id)
    except:
        return redirect("NotFound")

    if hasattr(request.user, 'student'):
        studentID = Student.objects.get(user=request.user)
        offlinerequest = OfflineRequest.objects.create(student=studentID, offlineclass=offlineclass)
        offlinerequest.save()
    return redirect("OfflineDetails", id=id)


@login_required(login_url='Login')
def OfflineOfferDetails(request, id):
    try:
        offlineoffer = OfflineOffer.objects.get(id=id)
    except:
        return redirect("NotFound")

    context = {
        "offlineoffer": offlineoffer,
    }

    if hasattr(request.user, 'student'):
        student = Student.objects.get(user=request.user)

        try:
            offlineofferrequest = OfflineOfferRequest.objects.get(student=student)
            isRequested = True
        except:
            isRequested = False

        context.update({"isRequested": isRequested})

    return render(request, 'offline-offer.html', context)


@login_required(login_url='Login')
def OfflineOfferEnroll(request, id):
    try:
        offlineoffer = OfflineOffer.objects.get(id=id)
    except:
        return redirect("NotFound")

    if hasattr(request.user, 'student'):
        studentID = Student.objects.get(user=request.user)
        offlineofferrequest = OfflineOfferRequest.objects.create(student=studentID, offlineoffer=offlineoffer)
        offlineofferrequest.save()
    return redirect("OfflineOffer", id=id)