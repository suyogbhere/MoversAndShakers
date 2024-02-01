from django.shortcuts import redirect, render
from django.contrib.auth import authenticate,login,logout
from .models import *
from datetime import date
from django.db.models import Q

# Create your views here.

def index(request):
    return render(request,'index.html')


# admin login
def admin_login(request):
    error = ''
    if request.method == 'POST':
        u = request.POST['username']
        p = request.POST['pwd']
        user = authenticate(username=u,password=p)
        try:
            if user.is_staff:
                login(request,user)
                error = 'no'
            else:
                error = 'yes'
        except:
            error = 'yes'
    return render(request,'admin_login.html',locals())


def admin_home(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    totalservices = Services.objects.all().count()
    readqueries = Contact.objects.filter(isread="yes").count()
    unreadqueries = Contact.objects.filter(isread="no").count()
    newbooking = SiteUser.objects.filter(status = None).count()
    oldbooking = SiteUser.objects.filter(status ="1").count()
    return render(request,'admin_home.html', locals())

def Logout(request):
    logout(request)
    return redirect(index)

def add_service(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    error = ""
    if request.method == 'POST':
        st = request.POST['servicetitle']
        ds = request.POST['description']
        ig = request.FILES['file']
        try:
            Services.objects.create(title=st, discription=ds, image=ig)
            error = "no"
        except:
            error = "yes"
    return render(request,'add_services.html',locals())


def manage_service(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    services = Services.objects.all()
    return render(request, 'manage_services.html',locals())




def edit_service(request,pk):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    service = Services.objects.get(id=pk)
    error = ""
    if request.method == 'POST':
        st = request.POST['servicetitle']
        ds = request.POST['description']
        
        service.title = st
        service.discription = ds
        try:
            service.save()
            error= "no"
        except:
            error = "yes"
        try:
            ig = request.FILES['file']
            service.image = ig
            service.save()
        except:
            pass
    return render(request, 'edit_service.html',locals())


def delete_service(request, pk):
    service = Services.objects.get(id=pk)
    service.delete()
    return redirect('manage_service')


def show_services(request):
    services = Services.objects.all()
    return render(request, 'show_services.html',locals())


def about(request):
    return render(request, 'about.html',locals())

def request_quote(request):
    error = ""
    if request.method == 'POST':
        nm = request.POST['name']
        em = request.POST['email']
        co = request.POST['contact']
        lo = request.POST['location']
        sl = request.POST['shiftingloc']
        sd = request.POST['shiftingdate']
        bi = request.POST['briefitems']
        it = request.POST['items']
        try:
            SiteUser.objects.create(name=nm,email=em,mobile=co,location=lo,shiftingloc=sl,shiftingdate=sd,updatationdate=sd,briefitems=bi,items=it,requestdate=date.today())
            error = "no"
        except:
            error = "yes"
    return render(request, 'request_quote.html',locals())


def new_booking(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    booking = SiteUser.objects.filter(status=None)
    return render(request, 'new_booking.html',locals())


def view_bookingdetail(request, pk):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    error = ''
    booking = SiteUser.objects.get(id=pk)
    if request.method == 'POST':
        remark= request.POST['remark']
        try:
            booking.remark = remark
            booking.status = '1'
            booking.updatationdate = date.today()
            booking.save()
            error = 'no'
        except:
            error='yes'
    return render(request, 'view_bookingdetail.html',locals())


def old_booking(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    booking = SiteUser.objects.filter(status="1")
    return render(request, 'old_booking.html',locals())


def delete_booking(request, pk):
    booking = SiteUser.objects.get(id=pk)
    booking.delete()
    return redirect('new_booking')


def contact(request):
    error = ""
    if request.method =='POST':
        nm = request.POST['name']
        co = request.POST['contact']
        em = request.POST['emailid']
        sb = request.POST['subject']
        ms = request.POST['message']
        try:
            contact = Contact.objects.create(name=nm,contact=co,emailid=em,subject=sb,message=ms,mdate=date.today(),isread="no")
            error ="no"
        except: 
            error = "yes"
    return render(request, 'contact.html',locals())


def unread_queries(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    contact = Contact.objects.filter(isread="no")
    return render(request, 'unread_queries.html',locals())


def read_queries(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    contact = Contact.objects.filter(isread="yes")
    return render(request, 'read_queries.html',locals())


def view_queries(request, pk):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    contact = Contact.objects.get(id=pk)
    contact.isread = "yes"
    contact.save()
    return render(request, 'view_queries.html',locals())


def delete_queries(request, pk):
    contact = Contact.objects.get(id=pk)
    contact.delete()
    return redirect('read_queries')



def search(request):
    error = ""
    if request.method =='POST':
        sd = request.POST['searchdata']
        try:
            booking = SiteUser.objects.filter(Q(name=sd)|Q(mobile=sd))
        except:
            booking=""
    return render(request, 'search.html',locals())


def betweendate_bookingreport(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    error = ""
    if request.method =='POST':
        fd = request.POST['fromdate']
        td = request.POST['todate']
        booking = SiteUser.objects.filter(Q(requestdate__gte=fd) & Q(requestdate__lte=td))
        return render(request, 'booking_betweendate.html',locals())    
    return render(request, 'betweendate_bookingreport.html',locals())


def betweendate_queryreport(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    error = ""
    if request.method =='POST':
        fd = request.POST['fromdate']
        td = request.POST['todate']
        booking = Contact.objects.filter(Q(mdate__gte=fd) & Q(mdate__lte=td))
        return render(request, 'query_betweendate.html',locals())    
    return render(request, 'betweendate_queryreport.html',locals())


def change_password(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    error = ""
    user = request.user
    if request.method =='POST':
        c = request.POST['currentpassword']
        n = request.POST['newpassword']
        try:
            if user.check_password(c):
                user.set_password(n)
                user.save()
                error = 'no'
        except:
            error = 'yes'
    return render(request, 'change_password.html',locals())