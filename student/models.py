from django.db import models

# Create your models here.
class Student(models.Model):
    student_no =models.CharField(max_length=100, unique=True)
    name =models.CharField(max_length=100,db_index=True)
    birthday=models.DateField()
    email=models.EmailField()

    def __str__(self):
        return self.student_no and self.student.name
    
    class Meta: 
        db_table ="student"

class Course(models.Model):
    name = models.CharField(max_length=100)
    credits= models.IntegerField()
    duration =models.IntegerField()

    def __str__(self):
        return self.name
    class Meta:
        db_table = "Course"

class Enrollment(models.Model):
    student = models.ForeignKey(Student,on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    date_enrolled = models.DateField()

    def __str__(self):
        return f"{self.student.name} enrolled in {self.course.name}"
    
    class Meta:
        db_table = "Enrollment"

