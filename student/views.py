from django.shortcuts import render, redirect, get_object_or_404
from .models import Student
from .forms import StudentForm
from django.contrib import messages

def create_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'student added successfully')
            return redirect('list_students')
        else:
            messages.error(request,'Oops! error occured')
    else:
        form = StudentForm
        return render(request, 'student/addstudent.html',{'form':form})




def list_students(request):
    students = Student.objects.all()
    return render(request, 'student/listtudent.html', {'students': students})

# You can add update and delete views below
def update_student(request, student_no):
    student = Student.objects.get(student_no=student_no)
    if request.method == 'POST':
       form = StudentForm(request.POST,instance=student)
       if form.is_valid():
          form.save()
          return redirect('list_students')
       else:
           messages.error(request, 'Oops! Error occured')
    else:
        form = StudentForm(instance=student)   
    return render(request, 'student/update.html', {'form': form,'student': student})

def delete_student(request, student_no):
    student = Student.objects.get(student_no=student_no)
    if request.method == 'POST':
        student.delete()
        messages.success(request,'Student deleted successfully')

        return redirect('list_students')
    return render(request, 'student/delete.html', {'student': student})

