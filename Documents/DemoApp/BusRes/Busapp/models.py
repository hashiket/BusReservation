from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class users(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)


    USER_TYPE_CHOICES = (
      ("cus", 'Customer'),
      ("bu", 'BusOwner'),
      ("abu", 'AdminBus'),
     )

    user_type = models.CharField(choices=USER_TYPE_CHOICES,max_length=100)

class Bus(models.Model):
    Bus_ID=models.AutoField(primary_key=True)
    Bus_name=models.CharField(max_length=30)
    Reg_No=models.IntegerField()
    Source=models.CharField(max_length=30)
    Destination=models.CharField(max_length=30)
    No_Seats=models.IntegerField()
    BO_ID=models.ForeignKey(User,related_name='BOID',on_delete=models.CASCADE)
    Status=models.BooleanField(default=True)

    rate=models.IntegerField()
    Deap_time=models.TimeField()
    Reach_time=models.TimeField()
    date=models.DateField()
    Av_Se=models.IntegerField()

    def __str__(self):
        return '%s'%(self.Bus_name)


class Reservation(models.Model):
    Reg_no=models.AutoField(primary_key=True)
    Cus_ID=models.ForeignKey(User,related_name="Cus_Id",on_delete=models.CASCADE)
    Bus_ID=models.ForeignKey(Bus,related_name="Bus_Id" ,on_delete=models.CASCADE)
#    Location=models.CharField(max_length=50)
#    Destination=models.CharField(max_length=50)
    time=models.TimeField()
    date=models.DateField()
    SeatsReser=models.IntegerField()
#TICKET_STATUSES = ((BOOKED, 'Booked'),
#                       (CANCELLED, 'Cancelled'),)
#status = models.CharField(choices=TICKET_STATUSES, default=BOOKED, max_length=255)

    def __str__(self):
        return '%s'%(self.Reg_no)


class SeatNo(models.Model):
    Seat_no=models.IntegerField()
    Regno=models.ForeignKey(Reservation,on_delete=models.CASCADE)


    def __str__(self):
        return '%s'%(self.Seat_no)
