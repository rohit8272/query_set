## to delete student whose id are same

>>> for i in range(n):
...     if queryset[i].stu_id == queryset[i+1].stu_id:
...             user = queryset[i]
...             user.delete()
...             i=i-1
...     else :
...             pass
