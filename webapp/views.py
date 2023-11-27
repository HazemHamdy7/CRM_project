
from django.shortcuts import render, redirect
from .forms import CreateUserForm, LoginForm, CreateRecordForm, UpdateRecordForm

from django.contrib.auth.models import auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate

from . models import Record
# Create your views here.


def home(request):
    context = {}
    return render(request, 'webapp/index.html', context)


# - Register

def register(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form .is_valid():
            form.save()
            return redirect('my_login')

    context = {'form': form}
    return render(request, 'webapp/register.html', context)

# - Login


def my_login(request):
    form = LoginForm()
    if request.method == "POST":
        form = LoginForm(request, data=request.POST)
        if form .is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(username=username, password=password)

            if user is not None:
                auth.login(request.user)
                return redirect('dashbord')
    context = {'form': form}
    return render(request, 'webapp/my-login.html', context)

#  - logout


def user_logout(request):
    auth.logout(request)

    return redirect('my_login')


#! -- - Dashbourd
@login_required(login_url='my_login')
def dashboard(request):
    my_record = Record.objects.all()

    context = {'records': my_record}
    return render(request, 'webapp/dashboard.html', context)


# ?  - Create a record
@login_required(login_url='my_login')
def create_record(request):
    form = CreateRecordForm()
    if request.method == 'POST':
        form = CreateRecordForm(request.POST)
        if form .is_valid():

            form.save()
            return redirect('dashboard')

    context = {'form': form}
    return render(request, 'webapp/create-record.html', context)


# ? - Updated a record
@login_required(login_url='my_login')
def update_record(request, pk):

    record = Record.objects.get(id=pk)
    form = UpdateRecordForm(instance=record)

    if request.method == 'POST':
        form = UpdateRecordForm(request.POST, instance=record)
        if form .is_valid():

            form.save()
            return redirect('dashboard')
    context = {'form': form}
    return render(request, 'webapp/update-record.html', context)


#  - Read / View a singler record
@login_required(login_url='my_login')
def singler_record(request, pk):

    all_record = Record.objects.get(id=pk)

    context = {'record': all_record}
    return render(request, 'webapp/view-record.html', context)


@login_required(login_url='my_login')
def delete_record(request, pk):

    record = Record.objects.get(id=pk)
    record.delete()

    return redirect('dashboard')
