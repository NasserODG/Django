from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

# Custommer's class
class Customer(models.Model):
    first_name = models.CharField(max_length=80)
    last_name = models.CharField(max_length=150)
    email = models.EmailField(max_length=253)
    phone_number = PhoneNumberField()
    address = models.CharField(max_length=70)
    city = models.CharField(max_length=60)
    country = models.CharField(max_length=40)
    
    def __str__(self):
        return self.first_name + ' ' + self.last_name
    
    class Meta:
        ordering = ['first_name', 'last_name']

# Vehicule type's class
class VehiculeType(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name    
    
# Vehicule size's class  
class VehiculeSize(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
        
# Vehicule's class
class Vehicule(models.Model):
    vehicule_type = models.ForeignKey(VehiculeType, related_name="Type", on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    real_cost = models.FloatField()
    vehicule_size = models.ForeignKey(VehiculeSize, related_name="Size", on_delete=models.CASCADE)

    def __str__(self):
        return str(self.vehicule_type)    


# Rental's class
class Rental(models.Model):
    rental_date = models.DateTimeField(auto_now_add=True)
    return_date = models.DateTimeField()
    customer = models.ForeignKey(Customer, related_name="customer", on_delete=models.CASCADE)
    vehicule = models.ForeignKey(Vehicule, related_name="vehicule", on_delete=models.CASCADE)

    def __str__(self):
        return str(self.vehicule)

    class Meta:
        ordering = ['rental_date']

# Rental rate's class
class RentalRate(models.Model):
    dayli_rate = models.FloatField()
    vehicule_type = models.ForeignKey(VehiculeType, on_delete=models.CASCADE)
    vehicule_size = models.ForeignKey(VehiculeSize, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.vehicule_type)