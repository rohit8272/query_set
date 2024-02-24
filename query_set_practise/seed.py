from faker import Faker
fake = Faker()
import random
from .models import *

def student_Marks(n):
    stu_obj = Student_details.objects.all()
    for student in stu_obj:
        subjects = StudentSubject.objects.all()
        for subject in subjects:
            StudentMarks.objects.create(
                student = student,
                subject = subject,
                marks = random.randint(0 ,100)
            )

def seed_db(n=10) -> None:
    for _ in range(n):
        department_obj = Department.objects.all()
        random_index = random.randint(0 , len(department_obj) - 1)
        department = department_obj[random_index]
        stu_id =  f'STU-{random.randint(100 ,999)}'
        stu_name = fake.name()
        stu_email = fake.email()
        stu_age = random.randint(20 , 30)
        stu_address = fake.address()

        stu_obj = Student_details.objects.create(
                   department = department,
                   stu_id = stu_id,
                   stu_name = stu_name,
                   stu_email = stu_email,
                   stu_age = stu_age,
                   stu_address = stu_address
                   )