from django.shortcuts import render,redirect
from .forms import Contact_Form
from django.contrib import messages
def home(request):
    if request.method=='POST':
        form=Contact_Form(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Your message has been sent successfully")
            form=Contact_Form()
            return redirect('/#contact')
        else:
            print(form.errors)     
    else:
        form=Contact_Form()    
    return render(request,'home.html',{'form':form})
# Create your views here.
