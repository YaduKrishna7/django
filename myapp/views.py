from django.shortcuts import render,redirect

# Create your views here.
from .forms import TableForm
from .models import Table

def tableview(request):
    if request.method == 'POST':
        form = TableForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('user_list')
    else:
        form = TableForm()
    return render(request,'table.html',{'form':form})

def user_list(request):
    users = Table.objects.all()
    return render(request,'user.html',{'users': users})