from django.shortcuts import render
from todoapp1.models import todo
# Create your views here.



def createtodo(request):
    if request.method == 'POST':
        name = request.POST['n']  # Retrieves the 'n' field from the form
        start_date = request.POST['s']  # Retrieves the 's' field
        is_checked = request.POST.get('a')  # Safely retrieves 'a' or returns None if not present
        print("Value of a:", is_checked)

        if is_checked is None:
            is_checked = False
        else:
            is_checked = True
        # Convert checkbox value to boolean

        # Save to the database
        todo.objects.create(
            name=name,
            date_time=start_date,
            is_true =  is_checked
        )

    return render(request,'todo1createhtml.html')


def show(request):
    f = todo.objects.all()
    return render(request, 'todo2showhtml.html' ,{"f":f})


def changetodo(request,p):
    f1 = todo.objects.get(id=p)
    f1.is_true = True
    f1.save()
    f = todo.objects.all()
    return render(request, 'todo2showhtml.html', {"f": f})