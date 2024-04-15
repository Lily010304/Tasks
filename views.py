from django.shortcuts import render

# Create your views here.

task = [ "foo", "bar", "baz"]
def index(request):
    return render(request, "tasks/taskli.html",
    { "task" : task;}
    )

