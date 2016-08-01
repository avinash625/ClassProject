from django.conf.urls import url
from studentMgmtApp.views import  *
from studentMgmtApp.classViews import  *
urlpatterns = [
    url(r'^$', view=TeacherHomeView , name = "TeacherHomeView" ),
    url(r'teacher/listStudents$',view=ListStudentView,name = "ListStudentView"),
    url(r'teacher/students/$',view = ListStudents, name = "ListStudents"),
    url(r'teacher/students/(?P<id>[0-9]+)/$',view=SingleStudentDetail,name = "SingleStudentDetail"),
    url(r'teacher/create/$',view = TeacherCreateView.as_view(), name = "TeacherCreateView"),
    url(r'teacher/addtest/$',view = TeacherAddTestView,name = "TeacherAddTestView"),
    url(r'teacher/addStudent/$',view = AddStudentView.as_view(),name = 'AddStudentView'),
    url(r'class/$',view = viewClasses.as_view(),name = "viewClasses"),
    url(r'class/create/$',view = CreateClass.as_view(), name = "CreateClassView"),
    url(r'class/(?P<id>[0-9]+)/students/$',view = ClassStudentsView,name = "ClassStudentView"),
]