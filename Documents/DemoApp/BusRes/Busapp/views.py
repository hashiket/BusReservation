from django.shortcuts import render

# Create your views here.
from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib.sessions.models import Session
from django.contrib import messages
from .models import users
from .models import Bus




# Create your views here.

def index(request):
    user=Bus.objects.all()
    return render(request,"Busapp/base.html",{'users':user})

def logout(request):
    auth.logout(request)
    return redirect('/')

def register(request):

    if request.method == 'POST':
        first_name=request.POST.get('first_name')
        print(first_name)
        last_name=request.POST.get('last_name')
        username=request.POST.get('username')
        password1=request.POST.get('password1')
        password2=request.POST.get('password2')
#        email=request.POST['email']
        if password1==password2:

             if User.objects.filter(username=username).exists():
                   messages.info(request,'Username Taken')
                   return redirect('register')

             else:

                  user=User.objects.create_user(first_name=first_name,last_name=last_name,username=username,password=password1)
#                  user=User.objects.create_user(first_name=first_name,last_name=last_name,username=username,password=password1)
#                 user.set_password(user.password)

        #          user.password=make_password(user.password)
                  user.save();

                  us=users(user=user,user_type="cus")
                  us.save();

                  print('user created')
                  return redirect('login')
                 # return redirect('/')


        else:
            messages.info(request,'password not matching...')
            return redirect('register')
        return redirect('/')

    else:
        return render(request,'Busapp/register.html')



def login(request):
    if request.method== 'POST':
        username=request.POST['username']
        password=request.POST['password']
        print(username)
        print(password)
        user=auth.authenticate(request,username=username,password=password)
#        user = Customer.objects.filter(username=username,password=password)
#        user=Customer.objects.get(username=username)
#        if user:
#            flag=check_password(password,user.password)
#            if flag:
#                return redirect("reservations")
#            else:
#                messages.info(request,"Invalid Credentials")
        user1=users.objects.filter(user=user)
        print(user1)
        b=0
        for a in user1:
            b=a.user_type

        if b =="cus" or b=="bu" or b=="abu" :
            if user is not None and b == "cus" :
                auth.login(request,user)
                #return redirect("/")
    #            request.Session['Cus_ID']=request.Post["username"]
    #            cusid=Customer.objects.get(username=username)

    #            re=Reservation.objects.get(Cus_ID='6')
    #            return redirect("reservations",{'bus':re})
                return redirect("reservations")
            else:
                messages.info(request,"Invalid Credentials")
                return redirect("login")
        else:
            messages.info(request,"Invalid Credentials")
            return redirect("login")

    else:
        return render(request,'Busapp/login.html')



def find(request):
    if request.method=='POST':
        source=request.POST['source']
        destination=request.POST['destination']
        date=request.POST.get('date')
        #date=request.POST['date']
        print(date)



        bus=Bus.objects.filter(Source=source,Destination=destination,date=date)
        #print(bus)
        b=0
        for bu in bus:
            b=bu.Bus_ID
            break
        a=b

        return render(request,"Busapp/find.html",{'buses':bus,'a':a,'source':source,'destination':destination,'date':date})
    elif request.method=="GET":
        source=request.GET.get('source')
        print(source)
        destination=request.GET.get('destination')
        date=request.GET['date']
        #date=request.POST['date']
        print(date)



        bus=Bus.objects.filter(Source=source,Destination=destination)
        #print(bus)
        b=0
        for bu in bus:
            b=bu.Bus_ID
            break
        a=b

        return render(request,"Busapp/find.html",{'buses':bus,'a':a,'source':source,'destination':destination,'date':date})
