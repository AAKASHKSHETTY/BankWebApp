from django.shortcuts import render, redirect
from sub.models import *

amt,amt1 = 0,0
cid,cid1= '',''
def home(request):
    return render(request, 'home.html')

def table(request):
    data = trans.objects.all()
    context = {'data':data}
    return render(request, 'table.html',context)

def cust(request):
    global amt,cid
    data = detail.objects.all()
    context = {'data': data,'tog': False}
    if request.method == 'POST':
        amt = int(request.POST.get('amt'))
        cid = request.POST.get('cid')
        context['tog'] = True
        context['from'] = cid
    return render(request, 'cust.html',context)

def sact(request):
    global amt,amt1,cid,cid1
    payer = detail.objects.get(Cust_id = cid)
    if request.method == 'POST':
        amt1 = int(request.POST.get('amt'))
        cid1 = request.POST.get('cid')
    payee = detail.objects.get(Cust_id = cid1)
    return render(request, 'sact.html',{'payer' : payer,'payee': payee})

def calc(request):
    global amt,amt1,cid,cid1
    if request.method == 'POST':
        amt2 = int(request.POST.get('amt'))
        if amt2 <= amt and amt2 > 0:
            amt1 += amt2
            amt -= amt2
            detail.objects.filter(Cust_id=cid).update(Amount=amt)
            detail.objects.filter(Cust_id=cid1).update(Amount=amt1)
            list = trans(payer_id=cid,payee_id=cid1,trans_amt=amt2)
            list.save()
        else:
            message = 'Enter a valid amount!'
            context={'mes': message}
            return render(request, 'sact.html',context)
    return render(request, 'cust.html')

def Add(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        amt = request.POST.get('amt')
        cid = request.POST.get('cid')
        loc = request.POST.get('loc')
        pictures = request.FILES.get('pictures')
        if name == '' or amt == '' or cid == '' or loc == '':
            msg = 'Enter all fields!'
            context = {'msg':msg}
            return render(request, 'Add.html',context)
        else:
            list = detail(Cust_id = cid,name=name ,location=loc, Amount=amt, img=pictures)
            list.save()
        return redirect('home')
    return render(request, 'Add.html')