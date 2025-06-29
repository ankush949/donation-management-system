from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import RegisterForm, LoginForm , DonationForm, ContactForm


# Create your views here.
def home_page(request):
    return render(request,'base.html')

def about_page(request):
    return render(request,'aboutus.html')


def donate_page(request):
    return render(request,'donate.html')

def register_page(request):
    if request.method=='POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user=form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            messages.success(request,"Account created Successfully!")
            return redirect('login')

    else:
        form = RegisterForm()
        return render(request,'register.html',{'form':form}) 
 
    
def login_page(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():

            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request,user)
                return redirect('home')
            else:
                form.add_error(None, "Invalid username or password")

    else:
        form = LoginForm()
    return render(request,'login.html',{'form':form})     

def logout_view(request):
    logout(request)
    return redirect('home')           


@login_required
def make_donation(request):
    if request.method == 'POST':
        form = DonationForm(request.POST)
        if form.is_valid():
            donation = form.save(commit=False)
            donation.user = request.user
            donation.save()
            return redirect('donation_success')
    else:
        form= DonationForm()
        return render(request,'make_donation.html',{'form':form})
        

def donation_success(request):
    return render(request,'donation_success.html')  

@login_required
def contact_page(request):
    if request.method =='POST':
        form = ContactForm(request.POST)    
        if form.is_valid():
            form.save()
            return redirect("contact_success")
    else:
        form = ContactForm()
    return render(request,'contact.html',{'form':form})   
     
def contact_success(request):
    return render(request,'contact_success.html')

def campaign_page(request):
    return render(request,'campaign.html')

