from django.shortcuts import render
from . models import contact_us
def home(request):
    return render(request,'home.html',{'page':'home'})

def about(request):
    return render(request,'about.html',{'page':'about'})

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        contact = contact_us(name = name,email = email , subject = subject , message = message)
        contact.save()
        print(name , email , subject , message)
        data = "Thanks for Contacting"
        return render(request,'contact.html', {'key': data ,'page':'contact'})
    
    return render(request,'contact.html',{'page':'contact'})

def services(request):
    return render(request,'services.html',{'page':'services'})

def resume(request):
    return render(request,'resume.html',{'page':'resume'})

def products(request):
    return render(request,'product.html',{'page':'products'})
