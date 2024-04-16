from django import forms
from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect
from . import templates
# Create your views here.

class NewTaskForm(forms.Form):
    task = forms.CharField(label = "New Task")


def index(request):
    if "tasks" not in request.session:
        request.session["tasks"] = []
    return render(request, "tasks/index.html", {
        "tasks": request.session["tasks"]
    })
    
def add(request):

    #add new task
    if request.method == "POST":
        #if it is a post that means user wants to add a new task so we will save it as form 
        form = NewTaskForm(request.POST)
        if form.is_valid():
            task = form.cleaned_data["task"]
            request.session["tasks"] += [task]
            return HttpResponseRedirect(reverse("tasks:index"))
           
        else :
            #if the input is invalid we wanna keep the info that the user put 
            return render(request, "tasks/add.html", {
            "form" : form})
              
    return render(request, "tasks/add.html", {
    "form" : NewTaskForm()}
    )
    

    

