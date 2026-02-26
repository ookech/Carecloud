from django.shortcuts import render,redirect,get_object_or_404

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

def delete(request, id):
    myappoint = MyAppoinments.objects.get(id = id)
    myappoint.delete()
    return render(request, 'show.html')
    return redirect('/show')

def edit(request, id):
    editappointment = get_object_or_404(MyAppoinments, id = id)

    if request.method == 'POST':
       editappointment.name = request.POST.get('name')
       editappointment.email = request.POST.get('email')
       editappointment.phone = request.POST.get('phone')
       editappointment.datetime = request.POST.get('date')
       editappointment.Department = request.POST.get('department')
       editappointment.Doctor = request.POST.get('doctor')
       editappointment.Message = request.POST.get('message')

       editappointment.save()
       return redirect('/show')

    else:
       return render(request, 'edit.html', {'editappointment': editappointment})

