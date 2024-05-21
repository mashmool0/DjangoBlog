from django.shortcuts import redirect
from django.contrib.auth.models import Group, User
from django.core.exceptions import ObjectDoesNotExist


def unauthenticated_user(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('home')
        else:
            return view_func(request, *args, **kwargs)

    return wrapper_func


def only_student_user(view_func):
    def wrapper_func(request, *args, **kwargs):
        try:
            user = request.user.groups.get(name='Student')
            return view_func(request, *args, **kwargs)
        except ObjectDoesNotExist:
            if request.user.is_superuser:
                return view_func(request, *args, **kwargs)
            return redirect('home')

    return wrapper_func


def only_teacher_user(view_func):
    def wrapper_func(request, *args, **kwargs):
        try:
            user = request.user.groups.get(name="Teacher")
            return view_func(request, *args, **kwargs)
        except ObjectDoesNotExist:
            if request.user.is_superuser:
                return view_func(request, *args, **kwargs)
            else:
                return redirect('home')

    return wrapper_func
