from django.shortcuts import render

from careapp.models import *


# Create your views here.
def home(request):
    return render(request, 'index.html')

def starter(request):
    return render(request, 'starter-page.html')

def appointment(request):
    if request.method == 'POST':
        all = MyAppoinments(
            name =  request.POST['name'],
            email = request.POST['email'],
            phone = request.POST['phone'],
            datetime = request.POST['date'],
            Department = request.POST['department'],
            Doctor = request.POST['doctor'],
            Message = request.POST['message'],
    )
    
        all.save()
        return render(request, 'appointment.html')
 
    else:
        return render(request, 'appointment.html')



def about(request):
    return render(request, 'about.html')

def show(request):
        allappointments = MyAppoinments.objects.all()
        return render(request, 'show.html', {'allappointments': allappointments})