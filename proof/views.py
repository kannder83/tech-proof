from django.shortcuts import get_object_or_404, redirect, render
from .models import Register
from .forms import RegisterForm


from rest_framework import viewsets
from django.http import Http404
from rest_framework import status
from rest_framework.response import Response

# Clase 'RegisterSerializer'
from .serializers import RegisterSerializer

# Create your views here.


def registers_list(request):
    registers = Register.objects.all()
    return render(request, 'proof/register_list.html', {
        'registers': registers
    })


def register_detail(request, pk):
    register = get_object_or_404(Register, pk=pk)
    return render(request, 'proof/register_detail.html', {'register': register})


def register_new(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            register = form.save(commit=False)
            register.save()
            return redirect('proof:register_detail', pk=register.pk)
    else:
        form = RegisterForm()
    return render(request, 'proof/register_edit.html', {'form': form})


def register_edit(request, pk):
    register = get_object_or_404(Register, pk=pk)
    if request.method == "POST":
        form = RegisterForm(request.POST, instance=register)
        if form.is_valid():
            register = form.save(commit=False)
            register.save()
            return redirect('proof:register_detail', pk=register.pk)
    else:
        form = RegisterForm(instance=register)
    return render(request, 'proof/register_edit.html', {'form': form})


def register_delete(request, pk):
    register = Register.objects.filter(pk=pk)
    register.delete()
    return render(request, 'proof/register_delete.html', {
        'msg': f'El registro con id {pk} fue eleminado.'
    })


# def register_by_city(request, city_name):
#     cities = Register.objects.filter(city=city_name)
#     return render(request, 'proof/cities_list.html', {
#         'cities': cities
#     })

class RegisterViewSet(viewsets.ModelViewSet):

    queryset = Register.objects.all().order_by('id')
    serializer_class = RegisterSerializer
