from django.shortcuts import render
from django.http import HttpResponse 
from .forms import LogForm,LogoutForm
import datetime as dt 
from .models import Log
# Create your views here.

def home(request):
    if request.method == 'POST':
        form = LogForm(request.POST)
        first_form = LogoutForm(request.POST)

        if form.is_valid():
            form.save()
            return HttpResponse('Success')
        elif first_form.is_valid():
            p = first_form.cleaned_data['id_number']
            Log.objects.filter(idNumber=p).update(out_time=dt.datetime.now())
            return HttpResponse('Successful')
    else:
        form=LogForm()    
        first_form = LogoutForm()
    return render(request, 'home2.html',{'form':form,'form1':first_form})
#def add1(request):
 #   val1=int(request.POST['id1'])
#def add2(request):
 #   val2=int(request.POST['id2'])