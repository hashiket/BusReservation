from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User,auth
from .models import Reservation,Bus,SeatNo
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from .models import users



def listbus(request):
    id=request.user.id
    bus=Bus.objects.filter(BO_ID=request.user.id)
#    bus=Bus.objects.all()
    return render(request,'Busapp/listbus.html',{'bus':bus})

def login_listbus(request):
    if request.method=='POST':
        username1=request.POST['username']
        password1=request.POST['password']

        user=auth.authenticate(username=username1,password=password1)

        user1=users.objects.filter(user=user)

        for a in user1:
            b=a.user_type


        if user is not None and b=="bu":
            auth.login(request,user)
            return redirect("BusOwner/listbus")
        else:
            messages.info(request,"Invalid Credentials")
            return redirect("login_listbus")
    else:
        return render(request,'Busapp/login_listbus.html')


def register_listbus(request):
    if request.method == 'POST':
        first_name=request.POST.get('first_name')
        last_name=request.POST.get('last_name')
        username=request.POST.get('username')
        password1=request.POST.get('password1')
        password2=request.POST.get('password2')
#        email=request.POST['email']
        if password1==password2:
              if User.objects.filter(username=username).exists():
                    messages.info(request,'Username Taken')
                    return redirect('register_listbus')

              else:
                  user=User.objects.create_user(username=username,password=password1,first_name=first_name,last_name=last_name)
#                  user=BusOwner(First_Name=first_name,Last_Name=last_name,username=username,password=password1)
                  user.save();

                  us=users(user=user,user_type="bu")
                  us.save();

                  print('user created')
        return redirect('login_listbus')


#        else:
#            messages.info(request,'password not matching...')
#            return redirect('register_listbus')
#        return redirect('/')
    else:
        return render(request,'Busapp/register_listbus.html')


def ViewRes(request):
    if request.method == "POST":
        bus=request.POST.get("bus_id")
        print(bus)
        team = Bus.objects.get(Bus_ID=request.POST.get("bus_id"))
        print(team)
        reser=Reservation.objects.filter(Bus_ID=bus)
        #reser=Reservation.objects.all()
        print(reser)
        seat=SeatNo.objects.all()
        #return redirect("reservations",{'res':reser})
        return render(request,"Busapp/ViewRes.html",{'res':reser})
    return render(request,"Busapp/ViewRes.html")
        #return render(request,"Busapp/reservationDetail.html")


def edit(request):
    if request.method =='POST':
        id=request.POST['bus_id']
        print(id)
        team = Bus.objects.filter(Bus_ID=id)
        return render(request,"Busapp/edit.html",{'bus':team})


def remove(request):
    if request.method == 'POST':
        id=request.POST['bus_id']
        print(id)
        bus=Bus.objects.filter(Bus_ID=id)
        bus.delete()
        bus=Bus.objects.filter(BO_ID=request.user.id)
    #    bus=Bus.objects.all()
        return render(request,'Busapp/listbus.html',{'bus':bus})
