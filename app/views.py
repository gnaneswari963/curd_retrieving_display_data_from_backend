from django.shortcuts import render
from app.models import *
from django.http import HttpResponse

# Create your views here.
def display_topic(request):
    QLTO=Topic.objects.all()
    d={'topic':QLTO}
    return render(request,'display_topic.html',context=d)

def display_webpage(request):
    QLWO=Webpage.objects.all()
    d={'webpage':QLWO}
    return render(request,'display_webpage.html',context=d)

def display_access_record(request):
    QLWO=AccessRecord.objects.all()
    d={'access_record':QLWO}
    return render(request,'display_access_record.html',context=d)