from django.shortcuts import render, redirect
from .form import UserForm
from .models import User


# Create your views here.


def employee_list(request):
    context = {'employee_list': User.objects.all()}
    return render(request, "employee_registration/employee_list.html", context)


def employee_form(request, id=0):
    if request.method == "GET":
        if id == 0:
            form = UserForm()
        else:
            employee = User.objects.get(pk=id)
            form = UserForm(instance=employee)
        return render(request, "employee_registration/employee_form.html", {'form': form})
    else:
        if id == 0:
            form = UserForm(request.POST)
        else:
            employee = User.objects.get(pk=id)
            form = UserForm(request.POST, instance=employee)
        if form.is_valid():
            form.save()
        return redirect('/emp/list')


def employee_delete(request):
    return
