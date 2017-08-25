from django.contrib.auth.models import User
from django.db import IntegrityError
from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone

from .models import Event, Profile, Ticket
from .forms import RegisterForm, LoginForm
from django.contrib.auth import authenticate, login, logout


def home(request):
    events = Event.objects.all()
    return render(request, 'eventsapp/event/list.html', {'events': events})


def user_logout(request):
    logout(request)
    return render(request, 'registration/logout.html')


def attend_event(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    try:
        Ticket.objects.create(user=request.user.profile, event=event)
    except IntegrityError:
        pass
    return redirect(event.get_absolute_url())


def event_detail(request, year, month, day, event):
    event = get_object_or_404(Event, slug=event,
                              created__year=year,
                              created__month=month,
                              created__day=day)
    all_tickets = Ticket.objects.filter(event=event)
    user_going = True if len(filter(lambda x: x.user.user == request.user, all_tickets)) > 0 else False
    datetime = timezone.now()
    return render(request, 'eventsapp/event/detail.html', {'event': event,
                                                           'all_tickets': all_tickets,
                                                           'user_going': user_going,
                                                           'datetime': datetime})


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(**cd)
            if user:
                login(request, user)
                return redirect("/")
            return render(request, 'registration/login.html', {'form': form,
                                                               'msg': 'username and password don\'t match'})
    else:
        form = LoginForm()
    return render(request, 'registration/login.html', {'form': form})


def user_register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            try:
                user = User.objects.create(username=cd['email'])
                user.first_name = cd['name']
                user.set_password(cd['password'])
                user.save()
                Profile.objects.create(user=user, sex=cd['sex'])
                return redirect("/login")
            except IntegrityError:
                print("error")
                return render(request, 'eventsapp/event/register.html', {'msg': "User already exist",
                                                                         'form': form})
    else:
        form = RegisterForm()
    return render(request, 'eventsapp/event/register.html', {'form': form})
