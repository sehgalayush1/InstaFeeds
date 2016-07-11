from django.shortcuts import get_object_or_404 ,render
from .models import College


def index(request):
    college_list = College.objects.all()
    context = {
    	'college_list' : college_list
    }
    return render(request,'college/index.html',context)

def detail(request,college_id):
    college = get_object_or_404(College,pk=college_id)
    context = {
    	'college' : college
    }
    return render(request,'college/detail.html',context)    