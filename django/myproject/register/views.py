from django.shortcuts import render, redirect
from .forms import RegisterForm

def register(response):
    err = ""
    
    if response.method == "POST":
        form = RegisterForm(response.POST)
        if form.is_valid():
            form.save()
            return redirect("/")
        else:
            err = form.errors
            
            
    print(err)

        
        
    form = RegisterForm()
    return render(response, "register/register.html", {"form":form, "error":err})