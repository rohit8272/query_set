from django.db import models

class Department(models.Model):
    department_name = models.CharField(max_length = 40)
    
    def __str__(self) -> str:
        return self.department_name
    
    class Meta:
        ordering = ['department_name']

class studnetManager(models.Manager):
    def get_queryset(self) -> models.QuerySet:
        return super().get_queryset().filter(is_deleted = False)

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
    is_deleted = models.BooleanField(default = False)
     
    objects = studnetManager()
    admin_objects = models.Manager()

    def __str__(self) -> str:
        return self.stu_name
    
    class Meta:
        ordering = ['stu_name']
    
class StudentMarks(models.Model):
    student = models.ForeignKey(Student_details , related_name = "student_marks" , on_delete = models.CASCADE)
    subject = models.ForeignKey(StudentSubject ,related_name = "student_subject" , on_delete = models.CASCADE)
    marks = models.IntegerField(default = 50)
    
    def __str__(self) -> str:
        return f'{self.student.stu_name} {self.subject.subject_name}'
    
    class Meta:
        unique_together = ['student' , 'subject']


class Studentrank(models.Model):
    student = models.ForeignKey(Student_details , related_name = "student_ranks" , on_delete = models.CASCADE)
    student_rank = models.IntegerField(default=1)
    created_at = models.DateField(auto_now_add = True)

    class Meta:
        unique_together = ['student_rank' , 'created_at']
        