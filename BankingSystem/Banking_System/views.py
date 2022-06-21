from django.shortcuts import render
from django.http import HttpResponse
from .models import Customers, Records

# Create your views here.

def index(request):
    return render(request,"index.html")

def customers(request):
    datas=Customers.objects.all()
    return render(request,"customers.html",{'datas':datas})

def transfer(request,id):
    costm=Customers.objects.get(id=id)
    recivers=Customers.objects.all().exclude(name=costm.name)
    return render(request,"transfer.html",{'costm':costm,'recivers':recivers})

def submission(request):
    vari = Records()
    vari.sender_name=request.POST.get('name')
    vari.resiver_name=request.POST.get('reciver')
    vari.transfer_balance=request.POST.get('balance')
    vari.save()
    send=Customers.objects.get(name=vari.sender_name)
    reci=Customers.objects.get(name=vari.resiver_name)
    send.balance=int(send.balance)-int(vari.transfer_balance)
    reci.balance=int(reci.balance)+int(vari.transfer_balance)
    send.save()
    reci.save()
    return HttpResponse("Transfer Successful")