from django.shortcuts import render
from django.http import HttpResponse
from .models import College


def index(request):
    college_list = College.objects.all()
    context = {
    	'college_list' : college_list
    }
    return render(request,'college/index.html',context)