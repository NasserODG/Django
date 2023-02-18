from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import CustomerForm, RentalForm
from django.contrib import messages
from django.core.paginator import Paginator
from .models import Customer, Vehicule, Rental
from faker import Faker

# Faker use
def faker_customer_view():
    fake = Faker()
    for _ in range(40):
        customer = Customer (
            first_name = fake.first_name(),
            last_name = fake.last_name(),
            email = fake.email(),
            phone_number = fake.phone_number(),
            address = fake.address(),
            city = fake.city(),
            country = fake.country()
        )
        customer.save()

# Vehicule list
def vehiculeList_view(request, id):
    if id == 0:
        vehicule = Vehicule.objects.all()
        page = Paginator(vehicule, 4)    
        pge = request.GET.get('page')
        cust = page.get_page(pge)
        var = 0
        return render(request, 'rent/vehiculeList.html', {'models': cust, 'len': var})
    else:
        vehicule = Vehicule.objects.filter(id=id)
        var = 1
        return render(request, 'rent/vehiculeList.html', {'models': vehicule, 'len': var})
    
#
def addVehicule_view(request):
        if request.method == 'POST':
            form = CustomerForm(request.POST)
            vehicule = Vehicule.objects.all()
            page = Paginator(vehicule, 4)
            pge = request.GET.get('page')
            cust = page.get_page(pge)
            if form.is_valid():
                form.save()
                messages.success(request, "Vehicule added !")
                return redirect('home')
            else:
                return render(request, 'rent/addVehicule.html', {"form": form, 'models': cust})
            
        else:
            form = CustomerForm()
            customer = Customer.objects.all()
            page = Paginator(customer, 5)
            pge = request.GET.get('page')
            cust = page.get_page(pge)
            
            return render(request, 'rent/addVehicule.html', {"form": form, 'models': cust})