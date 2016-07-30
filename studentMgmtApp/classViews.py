
from django.views.generic.list  import ListView
from django.views.generic.edit import CreateView , DeleteView, UpdateView
from studentMgmtApp.models import Teacher, Student, Class


class TeacherCreateView(CreateView):
    model = Teacher
    fields = ["teacherName","teacherDept","classes"]
    success_url = "/app/teacher/"

