from django.shortcuts import render, redirect
from .forms import RegisterForm, MilkRecordForm
from django.contrib import messages
from .models import Register, MilkRecord


# Create your views here.

# Registering members to the database

def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            firstName = form.cleaned_data['firstName']
            lastName = form.cleaned_data['lastName']
            email = form.cleaned_data['email']
            mobileNumber = form.cleaned_data['mobileNumber']
            Register.objects.create(firstName=firstName, lastName=lastName, email=email, mobileNumber=mobileNumber)
            messages.success(request, 'New Member has been added successfully')
            return redirect('register-url')
        else:
            messages.error(request, 'You have not been registered')
            return redirect('register-url')
    else:
        form = RegisterForm()

    # End of Registering members to the Database

    return render(request, 'dairy/register.html', {'form': form})


def all_members(request):
    registers = Register.objects.all()
    context = {
        'registers': registers,
    }
    return render(request, 'dairy/all_members.html', context=context)


def record_milk(request):
    form = MilkRecordForm()
    context = {
        "form": form
    }
    if request.method == "POST":
        form = MilkRecordForm(request.POST)
        if form.is_valid():
            farmer = form.cleaned_data["farmer"]
            milk_qty = form.cleaned_data["milk_qty"]
            milk_record = MilkRecord.objects.filter(farmer=farmer).first()
            if milk_record:
                milk_record.milk_qty += milk_qty
                milk_record.save()
            else:
                MilkRecord.objects.create(farmer=farmer, milk_qty=milk_qty)

    return render(request, 'dairy/record_milk.html', context=context)


def calculate_amount(request):
    milkrecords = MilkRecord.objects.all()
    context = {
        'milkrecords': milkrecords,
    }
    return render(request, 'dairy/calculate_amount.html', context=context)


def choose_activity(request):
    return render(request, 'dairy/choose_activity.html')
