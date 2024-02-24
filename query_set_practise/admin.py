from django.contrib import admin
from .models import *

admin.site.register(Department)
admin.site.register(Student_details)
admin.site.register(StudentSubject)

class Stu_marks_display(admin.ModelAdmin):
    list_display = ["student" ,"subject" , "marks"]

admin.site.register(StudentMarks ,Stu_marks_display)

