from django.urls import path
from . import views,views_Bowner,views_bus,views_admin,views_reser


urlpatterns=[
    path('',views.index,name="index"),
    path('logout',views.logout,name="logout"),
    path("register",views.register,name="register"),
    path('login',views.login,name="login"),
    path('BusOwner/listbus',views_Bowner.listbus,name='BusOwner/listbus'),
    path('BusOwner/login_listbus',views_Bowner.login_listbus,name="login_listbus"),
    path('BusOwner/register_listbus',views_Bowner.register_listbus,name="register_listbus"),
    path('BusOwner/bus',views_bus.bus,name='bus'),
    path('BusOwner/logout',views.logout,name="logout"),
    path('admin_bus',views_admin.admin_bus,name='admin_bus'),
    path('admin/busO',views_admin.data,name='adminBus/busO'),
    path('admin/buses',views_admin.buses,name='buses'),
    path('admin/logout',views.logout,name="logout"),
    path('users/reservations',views_reser.reservations,name="reservations"),
    path('users/bookseat1/reservationDetail',views_reser.reservationDetail,name='users/reservationDetail'),
    path('seat',views_reser.seat,name='seat'),
    path('seats',views_reser.seats,name='seats'),
    path('users/bookseat1/logout',views.logout,name="users/logout"),
    path('BusOwner/Reservation',views_Bowner.ViewRes,name='Reservation'),
    path('BusOwner/edit',views_Bowner.edit,name='edit'),
    path('BusOwner/update',views_bus.update,name='update'),
    path('users/bookseat1/find',views.find,name='users/find'),
    path('users/bookseat1/<int:id>',views_reser.bookseat1,name='bookseat1'),
    path('users/bookseat1/bookseat',views_reser.bookseat,name='bookseat'),
    path('users/bookseat1/seatno',views_reser.seatno,name='users/seatno'),
    path('users/bookseat1/delete',views_reser.deletedata,name='users/delete'),
    path('users/bookseat1/remove',views_Bowner.remove,name='users/remove'),
    path('users/bookseat1/reservations',views_reser.reservations,name="reservations"),






]
