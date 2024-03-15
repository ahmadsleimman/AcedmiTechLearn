from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import VIPClass, VIPCourse, VIPRequest, VIPMessage
from Main.models import Student, Teacher
# Create your views here.


def VIP(request):
    vipcourses = VIPCourse.objects.all()
    context = {
        "vipcourses": vipcourses,
    }
    return render(request, 'vip/vip.html', context)


@login_required(login_url='Login')
def VIPPrivateClass(request, id):
    try:
        vipclass = VIPClass.objects.get(id=id)
    except:
        return redirect("NotFound")

    vipmessages = VIPMessage.objects.filter(vipclass=vipclass)
    context = {
        "vipclass": vipclass,
        "vipmessages": vipmessages,
    }

    if hasattr(request.user, 'student'):
        isEnrolled = None
        student = Student.objects.get(user=request.user)

        if student == vipclass.student:
            isEnrolled = True

        context.update({"isEnrolled": isEnrolled})

    if hasattr(request.user, 'teacher'):
        isAdmin = None
        teacher = Teacher.objects.get(user=request.user)

        if teacher == vipclass.teacher:
            isAdmin = True

        context.update({"isAdmin": isAdmin})

    return render(request, 'vip/vip-private.html', context)


@login_required(login_url='Login')
def VIPDetails(request, id):
    try:
        vipcourse = VIPCourse.objects.get(id=id)
    except:
        return redirect("NotFound")

    context = {
        "vipcourse": vipcourse,
    }

    if hasattr(request.user, 'student'):
        student = Student.objects.get(user=request.user)

        try:
            vipclass = VIPClass.objects.get(vip_course=vipcourse, student=student)
            isEnrolled = True
            context.update({"vipclass": vipclass})
        except:
            isEnrolled = False

        try:
            viprequest = VIPRequest.objects.get(student=student, vip_course=vipcourse)
            isRequested = True
        except:
            isRequested = False

        context.update({"isEnrolled": isEnrolled})
        context.update({"isRequested": isRequested})

    if hasattr(request.user, 'teacher'):
        isAdmin = None
        teacher = Teacher.objects.get(user=request.user)

        if teacher == vipcourse.teacher:
            isAdmin = True

        context.update({"isAdmin": isAdmin})

    return render(request, 'vip/vip-details.html', context)


@login_required(login_url='Login')
def VIPEnroll(request, id):
    try:
        vipcourse = VIPCourse.objects.get(id=id)
    except:
        return redirect("NotFound")

    if hasattr(request.user, 'student'):
        studentID = Student.objects.get(user=request.user)
        viprequest = VIPRequest.objects.create(student=studentID, vip_course=vipcourse)
        viprequest.save()
    return redirect("VIPDetails", id=id)

