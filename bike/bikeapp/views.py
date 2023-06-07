from django.shortcuts import render,redirect
from .models import Bike
from .forms import BikeCreate
from django.http import HttpResponse
# Create your views here.

def index(request):
    shelf=Bike.objects.all()
    return render(request,'bike/library.html',{'shelf':shelf})

def upload(request):
    upload = BikeCreate()
    if request.method=='POST':
        upload=BikeCreate(request.POST,request.FILES)
        if upload.is_valid():
            upload.save()
            return redirect('index')
        else:
            return HttpResponse(""" Something went wrong. Please reload the webpage by clicking <a href="{{url:'index'}}>Reload</a>" """)
    else:
        return render(request,'bike/upload_form.html',{'upload_form':upload})
    
def update_bike(request,bike_id):
    bike_id=int(bike_id)
    try:
       bike_shelf=Bike.objects.get(id=bike_id)
    except Bike.DoesNotExist:
        return redirect('index')
    bike_form=BikeCreate(request.POST or None,instance=bike_shelf)
    if bike_form.is_valid():
        bike_form.save()
        return redirect('index')
    return render(request,'bike/upload_form.html',{'upload_form':bike_form}) 

def delete_bike(request,bike_id):
    bike_id=int(bike_id)
    try:
        bike_shelf=Bike.objects.get(id=bike_id)
    except Bike.DoesNotExist:
        return redirect('index')
    bike_shelf.delete()
    return redirect('index')