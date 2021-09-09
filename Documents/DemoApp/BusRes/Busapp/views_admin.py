from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User,auth
from .models import Reservation,Bus
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from .models import users



def admin_bus(request):
#    ad=User.objects.create_user(username="bhoyar",password="1234")
#    ad.save();
#    us=users(user=ad,user_type="abu")
#    us.save();


    if request.method=="POST":
        username=request.POST['username']
        password=request.POST['password']

        print(username,password)

        user=auth.authenticate(username=username,password=password)

        user1=users.objects.filter(user=user)
        b=0
        for a in user1:
            b=a.user_type

        if user is not None and b=="abu":
            auth.login(request,user)
            return redirect("admin/busO")

        else:
            messages.info(request,"Invalid Credentials")
            return redirect("admin_bus")
    else:

        return render(request,"Busapp/admin_bus.html")


@login_required
def data(request):
#    bus = Bus.objects.all()
    #bu=users.objects.filter(user_type="bu")
    #bo=User.objects.all()
    bo=users.objects.filter(user_type="bu")

    return render(request,"Busapp/data.html",{'bo':bo})
    #return render(request,"Busapp/data.html")

@login_required
def buses(request):
    if request.method=="POST":
#        fal=request.POST.get('dropdown')
#        fal=request.POST['dropdown']
#        id=request.POST['custId']
#        bus=Bus.objects.filter(pk=id).update(Status=fal)
#        bus.save()
        team = Bus.objects.get(Bus_ID=request.POST.get("bus_id"))
        if request.POST.get("status"):
            team.Status = request.POST.get("status")
            team.save()

    bus = Bus.objects.all()
    return render(request,"Busapp/buses.html",{'bus':bus})
    #return render(request,"Busapp/buses.html")
