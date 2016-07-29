from django.http.response import HttpResponse, HttpResponseNotFound
from django.shortcuts import render
from django.template.loader import get_template


# Create your views here.
from studentMgmtApp.models import Student


def TeacherHomeView(request):
    template = get_template("studentMgmtApp/TeacherHomeView.html")
    return HttpResponse(template.render())

def ListStudentView(request):
    students = Student.objects.all()
    template = get_template("studentMgmtApp/ListStudentView.html")
    return HttpResponse(template.render(context={"studentsList":students}))

def ListStudents(request):
    students = Student.objects.all()
    template = get_template("studentMgmtApp/liststudents.html")
    return HttpResponse(template.render(context={"students":students}))

def SingleStudentDetail(request,id):
    student = Student.objects.filter(id = id)
    template= get_template("studentMgmtApp/SingleStudentDetail.html")
    return HttpResponse(template.render(context={"student":student}))


