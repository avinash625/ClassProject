from django.conf.urls import url
from studentMgmtApp.views import  *
urlpatterns = [
    url(r'^teacher/$', view=TeacherHomeView , name = "TeacherHomeView" ),
    url(r'teacher/listStudents$',view=ListStudentView,name = "ListStudentView"),
    url(r'teacher/students/$',view = ListStudents, name = "ListStudents"),
    url(r'teacher/students/(?P<id>[0-9]+)/$',view=SingleStudentDetail,name = "SingleStudentDetail"),
]