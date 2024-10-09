from django.urls import path
from . import views

urlpatterns = [
    path('', views.create_student, name='create_student'),
    path('students/', views.list_students, name='list_students'),
    path('students/<str:student_no>/edit/', views.update_student, name='update_student'),
    path('students/<str:student_no>/delete/', views.delete_student, name='delete_student'),
]

