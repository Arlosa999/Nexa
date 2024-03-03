from django.shortcuts import render, redirect, get_object_or_404
from .models import Destination, Appointment
from .forms import DestinationForm, AppointmentForm


def homepage(request):
    destinations = Destination.objects.all()
    return render(request, 'myapp/homepage.html', {'destinations': destinations})


def add_destination(request):
    if request.method == 'POST':
        form = DestinationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('homepage')
    else:
        form = DestinationForm()
    return render(request, 'myapp/add_destination.html', {'form': form})


def destination_detail(request, id):
    destination = get_object_or_404(Destination, pk=id)
    return render(request, 'myapp/destination_detail.html', {'destination': destination})

def appointment_list(request):
    appointments = Appointment.objects.all()
    return render(request, 'myapp/appointment_list.html', {'appointments': appointments})

def create_appointment(request, destination_id):
    destination = get_object_or_404(Destination, pk=destination_id)

    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            appointment = form.save(commit=False)
            appointment.destination = destination
            appointment.save()
            return redirect('destination_detail', id=destination_id)
    else:
        form = AppointmentForm()
    
    return render(request, 'myapp/create_appointment.html', {'form': form, 'destination': destination})

def edit_appointment(request, appointment_id):
    appointment = get_object_or_404(Appointment, pk=appointment_id)
    if request.method == 'POST':
        form = AppointmentForm(request.POST, instance=appointment)
        if form.is_valid():
            form.save()
            return redirect('appointment_list')  # Redirect to appointment list after editing
    else:
        form = AppointmentForm(instance=appointment)
    return render(request, 'myapp/edit_appointment.html', {'form': form})

def delete_appointment(request, appointment_id):
    appointment = get_object_or_404(Appointment, pk=appointment_id)
    if request.method == 'POST':
        appointment.delete()
        return redirect('appointment_list')
    return render(request, 'myapp/delete_appointment.html', {'appointment': appointment})

def edit_destination(request, destination_id):
    destination = get_object_or_404(Destination, pk=destination_id)
    if request.method == 'POST':
        form = DestinationForm(request.POST, instance=destination)
        if form.is_valid():
            form.save()
            return redirect('destination_detail', id=destination_id)
    else:
        form = DestinationForm(instance=destination)
    return render(request, 'myapp/edit_destination.html', {'form': form})
