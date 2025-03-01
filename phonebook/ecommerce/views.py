from django.shortcuts import render

# Create your views here.
from decimal import Decimal
from datetime import date,timedelta
from django.shortcuts import render
from django.shortcuts import render, redirect
from .models import CustomUser,Product,Category,Order,OrderItem

def Register(request):
    if request.method == 'POST':
        username = request.POST['u']
        email = request.POST['e']
        wallet_balance = request.POST['w']

        # Save to the database
        h = CustomUser.objects.create(
            username=username,
            email=email,
            wallet_balance=wallet_balance
        )
        h.save()
        return home(request)

    return render(request, 'EREGISTER.html')



def home(request):
    hy = 0
    w = Order.objects.all()
    h = 0
    n = []
    t = {}
    h1 = {}
    h2 = {}
    records = 0
    sorted_h2 = ""
    today = date.today()
    seven_days_ago = today - timedelta(days=7)
    r  = Order.objects.all()
    thirty_days_ago = today - timedelta(days=30)
    six_months_ago = today - timedelta(days=180)
    for i in r:
        h = h + i.total_price
        if i.user.username in h1:
            h1[i.user.username] = h1[i.user.username] + 1

        else:
            h1[i.user.username] = 1
    for i in r:
        if  i.user.username in t:
            t[i.user.username] =   t[i.user.username] + i.total_price

        else:
            t[i.user.username] = i.total_price

        if i.user.created_at.date()  > seven_days_ago:
               print(Order)
               if i.user.username:
                  n.append(i.user.username)
        if i.user.created_at.date()  > thirty_days_ago:
               hy = hy + i.total_price

    u = CustomUser.objects.all()
    # try:
    u1 = Product.objects.all()
    for i in u1:
          if i.name in h2:
              h2[i.name] = h2[i.name] + 1
          else:
              h2[i.name] = 1
    print("h2",h2)
    top_users = sorted(t.items(), key=lambda x: x[1], reverse=True)[:3]
    print(top_users,"kkk")
    sorted_h2 = dict(sorted(h2.items(), key=lambda item: item[1], reverse=True)[:5])
    records = Product.objects.filter(category__created_at__range=(thirty_days_ago, today)).count()
    print("records",records)
    print(sorted_h2,"sorted_h2")
    d = OrderItem.objects.all()
    # except:
    #     print("it is comming here ")
    #     u1 = ""
    return render(request, 'Ehome.html',{'u':u,'p':u1,'n':n,'h':h,'h1':h1,"sorted_h2":sorted_h2,"records":records,"w":w,"d":d,"top_users":top_users,"hy":hy})  # Pass data to template


def login(request):

    return render(request, 'EODERS.html')  # Renders login form

def delete(request,p):
    u = CustomUser.objects.get(id=p)
    u.delete()
    return home(request)


def update(request,p):
    k = CustomUser.objects.get(id=p)
    if request.method == "POST":
        username = request.POST.get('u')
        print(username)
        email = request.POST['e']
        wallet_balance = request.POST['w']
        k.username = username
        k.email = email
        k.wallet_balance =   wallet_balance
        k.save()
        return home(request)
    print(k)
    return render(request, 'EUPDATE.html',{'k':k})  # Renders update page



def product(request):
    f = Product.objects.all()
    return render(request, 'Ehome.html',{'f':f})

def prodcreate(request):
    if request.method == "POST":
        username = request.POST.get('n')
        print(username)
        email = request.POST['p']
        wallet_balance = request.POST['s']
        category_id = request.POST['c']
        print(category_id)
        s = Category.objects.get(name=category_id)
        f = Product.objects.create(name=username,price=email,stock=wallet_balance,category=s)
        f.save()
        return home(request)
    categories = Category.objects.all()
    return render(request, 'Eprodcreate.html',{'categories':categories})


# Delete user


# Update user
def productupdate(request, p):
    p = Product.objects.get(id=p)
    categories = Category.objects.all()
    if request.method == "POST":
        p.name = request.POST.get('n')
        p.price = request.POST.get('p')
        p.stock = request.POST.get('s')
        category_id = request.POST['c']
        s = Category.objects.get(name=category_id)
        p.category = s
        p.save()
        return home(request)
    return render(request, 'Eprodupdate.html',{'i':p,'categories':categories})


def productdelete(request, p):
    p = Product.objects.get(id=p)
    p.delete()
    return home(request)


def toshowcategory(request,p):
    categories = Category.objects.all()
    g = Order.objects.filter(
       user__username=p)
    print(g)
    j = 0
    for i in g:
        j = i.total_price + j

    return render(request, 'Ecategory.html', {'categories': categories,"g":g,"j":j})

def showallproduct(request,p):
    c = Category.objects.get(id=p)
    c1 = Category.objects.get(name=c.name)
    p = Product.objects.filter(category=c1)
    print(p)
    return render(request, 'EShowproducts.html',{'p':p})

def atleastorder(request):
    n = []
    if request.method == "POST":
      username = request.POST.get('s')
      f = Order.objects.all()
      for i in f:
          if i.total_price > int(username):
              n.append(i)

    return render(request, 'Eatleastorder.html', {'n': n})


def atleastorderuser(request):
    n = []
    j = {}
    h = 0
    if request.method == "POST":
      username1 = request.POST.get('s')
      print(username1)
      # f = Order.objects.all()
      f =  Order.objects.prefetch_related('user').all()
      for i in f:
          if i.user.username in j:
              j[i.user.username] = j[i.user.username] + 1
          else:
              j[i.user.username] =  1
      print("it is j ", j)
      for i,k in j.items():
          if k >= int(username1):
              x = Order.objects.filter(user__username = i).first()
              n.append(x)
              print("it is n ",n)
      return render(request, 'EatleastorderUser.html', {'n': n})

    return render(request, 'EatleastorderUser.html', {'n': n})



def rodcreate(request):
    u = CustomUser.objects.all()
    if request.method == 'POST':
        user_id = request.POST.get('user')
        total_price = request.POST.get('total_price')
        status = request.POST.get('status')
        p = request.POST.get('p')
        q = request.POST.get('q')
        # Create and save the order
        e = Product.objects.filter(name=p).first()
        j=Order.objects.create(
            user_id=user_id,
            total_price=total_price,
            status=status
        )
        d = OrderItem.objects.create(
            order= j,
            product = e,
            quantity = q,
            subtotal_price =  int(q)*Decimal(j.total_price)

        )
        d.save()
        return home(request)
    status_choices = dict(Order.STATUS_CHOICES)
    context = {
        'users': CustomUser.objects.all(),
        'status_choices': status_choices,
    }
    return render(request, 'Erodcreate.html', context)
