from django.shortcuts import render, redirect, get_object_or_404
from .models import Event, Registration
from .forms import EventForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login


def register_page(request):
    if request.user.is_authenticated:
        return redirect('event_list')
    
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Registration successful')
            return redirect('event_list')
    else:
        form = UserCreationForm()
    return render(request, 'events/register.html', {'form':form})

def event_list(request):
    events = Event.objects.all().order_by('date', 'time')
    return render(request, 'events/event_list.html', {'events': events})

def event_detail(request, event_id):
    event = get_object_or_404(Event, pk = event_id)
    is_registered = False
    is_owner = False
    if request.user.is_authenticated:
        is_registered = Registration.objects.filter(event = event, user = request.user).exists()
        is_owner = event.created_by == request.user
    return render(request, 'events/event_detail.html', {'event': event, 'is_registered': is_registered, 'is_owner':is_owner})
    

@login_required
def event_create(request):
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            event = form.save(commit=False)
            event.created_by = request.user
            event.save()
            messages.success(request, 'Event created successfully')
            return redirect('event_list')  
    else:
        form = EventForm()
    
    
    return render(request, 'events/event_form.html', {'form': form})
        
@login_required
def register_event(request, event_id):
    event = get_object_or_404(Event, pk = event_id)
    Registration.objects.get_or_create(event = event, user = request.user)
    messages.success(request, 'You have registered for this event.')
    return redirect('event_detail', event_id = event.id)



def my_registration(request):
    registrations = Registration.objects.filter(user = request.user)
    return render(request, 'events/my_registrations.html', {'registrations': registrations})

@login_required
def delete_event(request, event_id):
    event = get_object_or_404(Event, pk = event_id)
    if event.created_by != request.user:
        return HttpResponseForbidden('You dont have permision to delete this event?!')
    if request.method =='POST':
        event.delete()
        messages.success(request, 'Event deleted successfully' )
        return redirect ('event_list')
    return render(request, 'events/event_confirm_delete.html', {'event':event})

@login_required
def edit_event(request, event_id):
    event = get_object_or_404(Event, pk = event_id)
    if event.created_by != request.user:
        return HttpResponseForbidden('You dont have permision to edit this event?!')
    if request.method == "POST":
        form = EventForm(request.POST, instance = event)
        if form.is_valid():
            form.save()
            messages.success(request, 'Event updated successfully')
            return redirect('event_detail', event_id = event.id)
    else:
     form = EventForm(instance = event)
     return render(request, 'events/event_edit.html', {'form':form, 'event':event})
    

@login_required
def leave_event(request, event_id):
    event = get_object_or_404(Event, id = event_id)
    user = request.user 
    registration = Registration.objects.filter(event=event, user=user)
    if registration.exists():
        registration.delete()
        messages.success(request, 'You have left this event')
    else:
        messages.error(request, 'You are not registered for this event')
    return redirect('event_detail', event_id = event.id)


    