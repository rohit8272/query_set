from django.db import models

class Department(models.Model):
    department_name = models.CharField(max_length = 40)
    
    def __str__(self) -> str:
        return self.department_name
    
    class Meta:
        ordering = ['department_name']

class StudentSubject(models.Model):
    subject_name = models.CharField(max_length = 100)
     
    def __str__(self) -> str:
        return self.subject_name

class Student_details(models.Model):
    department = models.ForeignKey(Department , related_name = "depart" ,on_delete = models.CASCADE)
    stu_id = models.CharField(max_length = 7)
    stu_name = models.CharField(max_length = 50)
    stu_email = models.CharField(unique = True,max_length = 50)
    stu_age = models.IntegerField(default = 18)
    stu_address = models.TextField()

    def __str__(self) -> str:
        return self.stu_name
    
    class Meta:
        ordering = ['stu_name']
    
class StudentMarks(models.Model):
    student = models.ForeignKey(Student_details , related_name = "student_marks" , on_delete = models.CASCADE)
    subject = models.ForeignKey(StudentSubject , on_delete = models.CASCADE)
    marks = models.IntegerField(default = 50)
    
    def __str__(self) -> str:
        return f'{self.student.stu_name} {self.subject.subject_name}'
    
    class Meta:
        unique_together = ['student' , 'subject']