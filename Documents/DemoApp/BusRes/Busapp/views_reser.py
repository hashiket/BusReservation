from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User,auth
from .models import Reservation,Bus,SeatNo
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required

@login_required
def reservations(request):

    if request.method== 'POST':
#        location=request.POST['location']
#        destination=request.POST['destination']
        #time=request.POST.get('time')
        #print(time)
        date=request.POST.get('total')

        id=request.POST['bus_id']

        seats=request.POST['no_seats']

        #username=request.POST['username']
#        cusid=Customer.objects.get(username=username)
        cusid=User.objects.get(id=request.user.id)

        regno=request.POST.get('regno')
        stno=request.POST.get('st')

    #    for s in no_seats:
    #        ha=Reservation.objects.filter(Reg_no=33)
    #        s=SeatNo(Seat_no=s,Reg_no=ha)
    #        s.save();

        time="10:00"
        date="2021-01-15"

        if len(stno)==1:
            messages.info(request,"Please select seat..")
            return redirect("bookseat1",id)

        busid=Bus.objects.get(Bus_ID=id)
        raw=(busid.Av_Se-int(seats))+1
        if raw <= 0:
            busid.Av_Se=0
            messages.info(request,"Seats are not available..")
            return redirect("bookseat1",id)
        else:
            busid.Av_Se=raw


        busid.save()




    #    user1=Reservation(time=time,date=date,SeatsReser=no_seats,Bus_ID=busid,Cus_ID=cusid)
        #user1=Reservation.objects.create(SeatsReser=int(seats)-1,Bus_ID=busid,Cus_ID=cusid,time=time,date=date)


    #    instance=user1.save();
        print('reservation success')



        has=''
        count=0
        for stn in stno:

            if stn != ',':
                has=has+stn
                count=count+1

                if  count==2:
                    count=0
                    print(has)
                    print()
                    has=''
            else :

                print(has)
                has=''



        has=''
        count=0
        count1=0
        for stn in stno:
          if count1>1:
            if stn != ',':
                count=count+1
                has=has+stn
                if  count==2:
                    if SeatNo.objects.filter(Seat_no=has).exists():
                       messages.info(request,"Selected seat is occupied")
                       return redirect("bookseat1",id)
                    else:

                        count=0
                        has=''
            else:
                if has :
                   if SeatNo.objects.filter(Seat_no=has).exists():
                     messages.info(request,"Selected seat is occupied")
                     return redirect("bookseat1",id)
                   else:

                        has=''
          count1=count1+1




    #    ha=Reservation.objects.get(Reg_no="53")

        user1=Reservation.objects.create(SeatsReser=int(seats)-1,Bus_ID=busid,Cus_ID=cusid,time=time,date=date)

        ha=Reservation.objects.get(Reg_no=user1.pk)
    #    ha='id'
        has=''
        count=0
        count1=0
        for stn in stno:
          if count1>1:
            if stn != ',':
                count=count+1
                has=has+stn
                if  count==2:
                        s=SeatNo(Seat_no=int(has)-1,Regno=ha)
                        s.save();
                        count=0
                        has=''
            else:
                count=0
                if has :

                        s=SeatNo(Seat_no=int(has)-1,Regno=ha)
                        s.save();
                        has=''
          count1=count1+1

        #reser=Bus.objects.filter(Reg_No=regno)
        #return render(request,'Busapp/reservation.html',{'bus':reser})
        #return render(request,'Busapp/reservation.html')



        messages.info(request,"Successful Reservation")

        return redirect('reservations')


    #    print(stno)
    #    st=stno.split(",")
    #    print(st)
    #    for i in st:
    #        s=SeatNo(Seat_no=i,Reg_no=reservations.request.id)
    #        s.save();

    else:
#        reser=Bus.objects.filter(Reg_No=12)
        #bus=Bus.objects.all()
        #return render(request,'Busapp/reservation.html',{'buses':bus})
        return render(request,'Busapp/reservation.html')


@login_required
def seats(request):
    return render(request,'Busapp/seats.html')


@login_required
def reservationDetail(request):
    reser=Reservation.objects.filter(Cus_ID=request.user.id)
    #reser=Reservation.objects.filter(Cus_ID=6)
    print(reser)
    seat=SeatNo.objects.all()
    return render(request,"Busapp/reservationDetail.html",{'res':reser})
    #return redirect('reservationDetail')

def seat(request):
    return render(request,'Busapp/seat.html')


def seats(request):
    return render(request,'Busapp/seats.html')


def bookseat(request):
    if request.method=='POST':
        id=request.POST['bus_id']
        bus=Bus.objects.filter(Bus_ID=id)
        for bu in bus:
            cou=bu.No_Seats
        h=''
        count=0
        for co in range(int(cou/5)):
            h=h+'1'
            count=count+1

        print(h)
        print(count)
        seatsno=SeatNo.objects.all()
        return render(request,'Busapp/seats1.html',{'bus':bus,'ha':h,'count':count,'seatsno':seatsno})
    


        #return redirect('reservations/find')


def bookseat1(request,id):
        bus=Bus.objects.filter(Bus_ID=id)
        for bu in bus:
            cou=bu.No_Seats
        h=''
        count=0
        for co in range(int(cou/5)):
            h=h+'1'
            count=count+1
        print(h)
        seatsno=SeatNo.objects.all()
        return render(request,'Busapp/seats1.html',{'bus':bus,'ha':h,'count':count,'seatsno':seatsno})


def seatno(request):
    if request.method=='POST':
        regno=request.POST['regno']
        print(regno)
        seat=SeatNo.objects.filter(Regno=regno)
        return render(request,"Busapp/reservationDetail.html",{'seat':seat})

def deletedata(request):
    if request.method=='POST':
        regno=request.POST['regno']
        #seat=request.POST['seats']
        #bus_id=request.POST['bus_id']
        #rate=request.POST['rate']
        #dtime=request.POST['dtime']
        #print(dtime)
        #print(rate)
        #bus=Bus.objects.filter(Bus_name=bus_id,rate=rate)
        #print(bus)
        #print(bus.rate)
        #bus.Av_Se=bus.Av_Se + int(seat)
        #bus.save()


        reg=Reservation.objects.filter(Reg_no=regno)
        reg.delete()
        print(reg)


        reser=Reservation.objects.filter(Cus_ID=request.user.id)
        print(reser)
        return render(request,"Busapp/reservationDetail.html",{'res':reser})
