from django.shortcuts import render
from django.core.paginator import Paginator
from .models import *
from django.db.models import Q

def get_data(request):
    query_set = Student_details.objects.all()

    if request.GET.get("search"):
        search = request.GET.get("search")
        query_set = query_set.filter(
            Q(stu_name__icontains = search) |
            Q(stu_id__icontains = search) |
            Q(stu_email__icontains = search) |
            Q(stu_age__icontains = search) |
            Q(stu_address__icontains = search) |
            Q(department__department_name__icontains = search)  
        )

    paginator = Paginator(query_set , 15)
    page_no = request.GET.get("page" , 2)
    page_object = paginator.get_page(page_no)

    context = {"student_data" : page_object}
    return render(request , "students.html" , context )


