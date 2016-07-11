from django.shortcuts import render,get_object_or_404
from .models import Society


def index(request):
    society_list = Society.objects.all()
    context = {
    	'society_list' : society_list
    }
    return render(request,'society/index.html',context)

def detail(request,society_id):
    society = get_object_or_404(Society,pk=society_id)
    context = {
    	'scoiety' : society
    }
    return render(request,'society/detail.html',context)
