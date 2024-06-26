from django.shortcuts import render, redirect
from .forms import ContactUsForm, MessagesForm, AuthenticationForm, UserEditForm, RegisterForm
from home.models import Messages
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User, Group
from django.views.generic.base import View
from django.shortcuts import HttpResponse
from django.views.generic import TemplateView
from .decorators import unauthenticated_user, only_student_user
from django.contrib.auth.decorators import login_required


# Create your views here.
def contact(request):
    if request.method == "POST":
        form = MessagesForm(request.POST)
        if form.is_valid():
            # form.save() # you can save every thing without any changing
            instance = form.save(commit=False)
            instance.title += "-Owner"
            instance.save()
            # title = form.cleaned_data.get("title")
            # text = form.cleaned_data.get('text')
            # Messages.objects.create(title=title, text=text)
            # return redirect('contactus_app:contactus')
        else:
            print("chakhan")
    else:
        form = MessagesForm()

    return render(request, 'account/contact.html', context={'form': form})


@unauthenticated_user
def user_login(request):
    if request.method == "POST":
        form = AuthenticationForm(request.POST)
        if form.is_valid():
            user = User.objects.get(username=form.cleaned_data.get('username'))
            print(user)
            login(request, user)
            return redirect('home')
        else:
            print('valid nabood ')

    else:
        print('post nabood ')
        form = AuthenticationForm()
    return render(request, 'account/authentication.html', context={"form": form})


@unauthenticated_user
def user_register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            user = User.objects.create_user(username=form.cleaned_data.get('fullname'),
                                            password=form.cleaned_data.get("password1"))
            user.groups.add(Group.objects.get(name="Student"))
            print("HI")
            login(request, user)
            return redirect('home')
        else:
            print("Form is not valid")
    else:
        print("post nabood")
        form = RegisterForm()

    return render(request, 'account/register.html', {'form': form})


@login_required(login_url="/account/login")
def user_logout(request):
    logout(request)
    return redirect('home')


@login_required(login_url="/account/login")
def user_edit(request):
    user = request.user
    form = UserEditForm(instance=user)
    if request.method == "POST":
        form = UserEditForm(instance=user, data=request.POST)
        if form.is_valid():
            form.save()

    return render(request, 'account/edit.html', context={"form": form})


@only_student_user
def student_information(request):
    return render(request, 'account/information.html', context={})
