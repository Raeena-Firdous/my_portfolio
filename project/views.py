from django.shortcuts import render
from django.http import HttpResponse
from project.models import Contact

# Create your views here.
def home(request):
#    return HttpResponse("<h1>hello raeena</h1>")
    return render(request, 'home.html')

def about(request):
#    return HttpResponse("<h1>about raeena</h1>")
    return render(request, 'about.html')

def project(request):
#    return HttpResponse("<h1>raeena project</h1>")
    return render(request, 'project.html')

def contact(request):
    if request.method=='POST':
        print("This is a post")
        name=request.POST['name']
        email=request.POST['email']
        phone=request.POST['phone']
        desc=request.POST['desc']
        print(name,email,phone,desc)
        ins =Contact(name=name,email=email,phone=phone,desc=desc)
        ins.save()
        print('the data has been written to the db')
#    return HttpResponse("<h1>raeena's contact</h1>")
    return render(request, 'contact.html')

def education(request):
    return render(request, 'education.html')

def skills(request):
    return render(request, 'skills.html')

def internships(request):
    return render(request, 'internships.html')