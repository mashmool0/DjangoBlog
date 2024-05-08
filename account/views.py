from django.shortcuts import render, redirect
from .forms import ContactUsForm, MessagesForm, AuthenticationForm, UserEditForm
from home.models import Messages
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User


# Create your views here.
def contact(request):
    form = MessagesForm()
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
        print("chakhan2")

    return render(request, 'account/contact.html', context={'form': form})


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


def user_logout(request):
    logout(request)
    return redirect('home')


def user_edit(request):
    user = request.user
    form = UserEditForm(instance=user)  # instance yani taraf vaghti miad input haro bebine barash khodkar m
    # izare mager bakhed taghir bedee khodesh
    if request.method == "POST" :
        form = UserEditForm(instance=user,data=request.POST)
        if form.is_valid() :
            form.save()

    return render(request, 'account/edit.html',context={"form":form})
