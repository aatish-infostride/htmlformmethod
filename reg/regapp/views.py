from django.shortcuts import render

from .forms import regform

# Create your views here.

def signup(request):
    form= regform(request.POST or None)
    if form.is_valid():
        form.save()

    context = {'form':form}
    return render(request,'index.html',context)
        