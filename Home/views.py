from django.shortcuts import render
from datetime import datetime
from .models import Contact
from django.contrib import messages


def Home(request):
    return render(request,'home/index.html')

#About
def About(request):
    return render(request,'home/about.html')

#contact
def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('area')
        contacted = Contact(name=name.title(), email=email, phone=phone, desc=desc, date=datetime.today())
        contacted.save()
        messages.success(request, 'Your message has been successfully send.')
        return render(request,'home/index.html')
    return render(request,'home/contact.html')

def digitalservice(request):
    return render(request,'services/digitalmarketing.html')

def socialmediaservice(request):
    return render(request,'services/socialmedia.html')

def webdesignservice(request):
    return render(request,'services/webdesign.html')

def contentwritingservice(request):
    return render(request,'services/contentwriting.html')

def graphicdesignservice(request):
    return render(request,'services/graphicdesign.html')