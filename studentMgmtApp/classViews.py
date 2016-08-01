
from django.views.generic.list  import ListView
from django.forms import Textarea , TextInput
from django.views.generic.edit import CreateView , DeleteView, UpdateView
from studentMgmtApp.models import Teacher, Student, Class


class TeacherCreateView(CreateView):
    model = Teacher
    fields = ["teacherName","teacherDept","classes"]
    success_url = "/app/teacher/"

class AddStudentView(CreateView):
    model = Student
    fields = ["studentName","studentYear","studentDept","studentClass"]
    success_url = "/app/teacher/listStudents"
    widgets = {
        'StudentName': TextInput(),
    }

class viewClasses(ListView):
    model = Class
