## to delete student whose id are same

>>> for i in range(326):
...     if queryset[i].stu_id == queryset[i+1].stu_id:
...             user = queryset.filter(stu_id = queryset[i].stu_id)
...             user.delete()
