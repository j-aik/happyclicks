from django.shortcuts import render
from django.shortcuts import render
from bookapp.models import Books

from bookapp.forms import BookForm

# Create your views here.



def home(request):
    k = Books.objects.all()
    return render(request,'home.html',{'k':k})



def phonebookadd(request):
    return render(request,'create.html',)



def phonebookadded(request):
    if (request.method == "POST"):
        T = request.POST['T']
        A = request.POST['A']
        b = Books.objects.create(name=T, Phone_number=A)
        b.save()
    return home(request)



def phonebookedit(request,p):
    b = Books.objects.get(id=p)
    if (request.method == "POST"):
        form = BookForm(request.POST, request.FILES, instance=b)
        if form.is_valid():
            form.save()
            return home(request)

    form = BookForm(instance=b)
    return render(request,'edit.html',{'b':form})


def uudelete(request,p):
    b = Books.objects.get(id=p)
    b.delete()
    return home(request)


def editbook(request):
     return render(request,'home.html')


