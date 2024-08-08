from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from cars.models import Car

# View to list all cars
def carlist(request):
    allcars = Car.objects.all()
    return render(request, 'cars/carlist.html', {'allcars': allcars})

# View to add a new car
def add(request):
    if request.method == 'POST':
        brand = request.POST.get('brand')
        country = request.POST.get('country')
        year = int(request.POST.get('year'))

        Car.objects.create(brand=brand, country=country, year=year)
        messages.success(request, 'Car added successfully')
        return redirect(reverse('cars:carlist'))
    else:
        return render(request, 'cars/add.html')
    
    
# View to update a car
def update(request, pk):
    car = get_object_or_404(Car, pk=pk)  # Get the car object to be updated
    
    if request.method == 'POST':
        brand = request.POST.get('brand')
        country = request.POST.get('country')
        year = request.POST.get('year')
        
        # Update the car object with the new values
        car.brand = brand
        car.country = country
        car.year = year
        car.save()
        
        messages.success(request, 'Car updated successfully')
        return redirect(reverse('cars:carlist'))
    
    return render(request, 'cars/update.html', {'car': car})

# View to delete a car
def delete(request):
    if request.method == 'POST':
        pk = request.POST.get('pk')
        try:
            car = Car.objects.get(id=pk)
            car.delete()
            messages.success(request, 'Car deleted successfully')
        except Car.DoesNotExist:
            messages.error(request, 'Car not found')
        except Exception as e:
            messages.error(request, f'Error deleting car: {e}')
        return redirect(reverse('cars:carlist'))
    else:
        # Redirect to the car list if accessed via GET
        return render(request, 'cars/delete.html')
