from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User,auth
from .models import Reservation,Bus
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required


@login_required
def bus(request):
    if request.method=='POST':
        busname=request.POST['busname']
        #regno=request.POST['regno']
        source=request.POST['source']
        print(source)
        destination=request.POST['destination']
        no_seats=request.POST['seats']
        status="True"
        Dtime=request.POST['Dtime']
        Rtime=request.POST['Rtime']
        rate=request.POST['rate']
        date=request.POST['date']

        bo=User.objects.get(id=request.user.id)
#        print(user)
#        pk=BusOwner.objects.get(BO_ID=bo)
#        pk=BusOwner.objects.get(BO_ID="2")

        user=Bus(Bus_name=busname,Source=source,Destination=destination,No_Seats=no_seats,Status=status,BO_ID=bo,Deap_time=Dtime,Reach_time=Rtime,rate=rate,Reg_No=12,date=date,Av_Se=no_seats)
        user.save();
        print('Bus registered')
        return redirect('BusOwner/listbus')
    return render(request,"Busapp/bus.html")


def update(request):
    if request.method=='POST':
        id=request.POST['id']
        busname=request.POST['busname']
        #regno=request.POST['regno']
        source=request.POST['source']
        destination=request.POST['destination']
        no_seats=request.POST['seats']
        status="True"
        Dtime=request.POST['Dtime']
        Rtime=request.POST['Rtime']
        rate=request.POST['rate']
        date=request.POST['date']

        bo=User.objects.get(id=request.user.id)
#        print(user)
#        pk=BusOwner.objects.get(BO_ID=bo)
#        pk=BusOwner.objects.get(BO_ID="2")

        #user=Bus(Bus_name=busname,Reg_No=regno,Source=source,Destination=destination,No_Seats=no_seats,Status=status,BO_ID=bo,Deap_time=Dtime,Reach_time=Rtime,rate=rate)
        user=Bus.objects.get(Bus_ID=id)
        user.Bus_name=busname;
        #user.Reg_No=regno;
        user.Source=source;
        user.Destination=destination;
        user.No_Seats=no_seats;
        user.Deap_time=Dtime;
        user.Reach_time=Rtime;
        user.rate=rate;
        user.date=date;

        user.save();
        print('Bus registered')
        return redirect('BusOwner/listbus')
    return render(request,"Busapp/bus.html")
