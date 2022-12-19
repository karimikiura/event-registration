from django.shortcuts import render, get_object_or_404, redirect, HttpResponseRedirect

from django.contrib import messages

from .models import Event, Submission

from core.accounts.models import CustomUser
from .forms import ProjectSubmissionForm

def home_page(request):
    users = CustomUser.objects.filter(hackthon_participant=True)
    events = Event.objects.all()

    context = {
        'events': events,
        'users': users,
        'title': 'Home',
    }
    return render(request, 'home.html', context)


def profile_page(request, pk):
    user = get_object_or_404(CustomUser, id=pk)
    context = {
        'title': "Profile Section",
        "user": user,
    }

    return render(request, 'profile.html', context)


def account_page(request):
    user = request.user
    context = {
        'user': user,
        'title': "Account Page"
    }
    return render(request, 'account.html', context)


def event_page(request, event_id):
    event = get_object_or_404(Event, pk=event_id)

    # get events user is registered for -> move to model method, if user registerd, disable reg button
    registered = request.user.events.filter(id=event.id).exists()
    submitted = Submission.objects.filter(participant=request.user, event=event).exists()
    # print("You're registerd for:", registered)
    context = {
        'event': event, 
        'registered':registered,
        'submitted':submitted,
        'title': 'Event Detail',
    }
    return render(request, 'event.html', context)

def registration_confirmation(request, event_id):
    event = get_object_or_404(Event, pk=event_id)
    
    if request.method == 'POST':
        # event = Event.objects.get(id=request.POST.get('event'))
        # print(event) 
        print(request.user)
        event.participants.add(request.user)
        messages.success(request, 'Your event registration has been confirmed')
        return redirect('event:event', event_id=event.id)
    # else:
    #     return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    context = {
        'event': event,
    }
    return render(request, 'event_confirmation.html', context)
    

def project_submission(request, pk):
    event = get_object_or_404(Event, id=pk)
    if request.method == 'GET':
        form = ProjectSubmissionForm()

    if request.method == 'POST':
        form = ProjectSubmissionForm(request.POST or None)
        if form.is_valid():
            form_payload = form.save(commit=False)
            form_payload.participant = request.user
            form_payload.event = event
            form_payload.save()
        
        messages.success(request, "Project has been submitted successfully.")
        return redirect('event:profile', pk=event.id)

    context = {
        'event': event,
        'title': "Submit Project",
        'form': form,
    }
    return render(request, 'submit_form.html', context)


def update_submission(request, pk):
    submission = get_object_or_404(Submission, pk=id)
    event = get_object_or_404(Event, id=pk)
    form = ProjectSubmissionForm(instance=submission)
    context = {
        'submission': submission,
        'form': form,
    }

    return render(request, 'update_submission.html', context)

