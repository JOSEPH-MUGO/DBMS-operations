from django import forms
from . models import *


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['student_no', 'name', 'birthday','email']
        widgets = {
            'birthday': forms.DateInput(attrs={'type': 'date'}),
        }

class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['name', 'credits', 'duration']

class EnrollmentForm(forms.ModelForm):
    class Meta:
        model = Enrollment
        fields = ['student', 'course', 'date_enrolled']
        widgets = {'date_enrolled': forms.DateInput(attrs={'type':'date'})},