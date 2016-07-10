from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the College List From Here Select a college to Go to Your Collge page")
