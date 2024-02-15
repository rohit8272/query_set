from django.db import models

class Department(models.Model):
    department_name = models.CharField(max_length = 40)
    
    def __str__(self) -> str:
        return self.department_name
    
    class Meta:
        ordering = ['department_name']
  

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
    
