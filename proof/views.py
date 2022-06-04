from datetime import date
from django.shortcuts import get_object_or_404, redirect, render
from .models import Register
from .forms import RegisterForm


from rest_framework import viewsets
from django.http import Http404
from rest_framework import status
from rest_framework.response import Response

# Clase 'RegisterSerializer'
from .serializers import RegisterSerializer

from django.db.models import Count

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
            count_of_cities = Register.objects.filter(
                city__iexact=form.cleaned_data["city"]).count()

            legal_age = date.today() - form.cleaned_data["date_of_birth"]

            if legal_age.days < 365*17:
                return render(request, 'proof/msg.html', {
                    "msg": "No es mayor de edad"
                })

            if count_of_cities < 3:
                register = form.save(commit=False)
                register.save()
                return redirect('proof:register_detail', pk=register.pk)
            else:
                return render(request, 'proof/msg.html', {
                    "msg": f'La ciudad {form.cleaned_data["city"]} ya ha sido registrada 3 veces.'
                })
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


def register_filter_by_city(request, city):
    count = Register.objects.filter(city__iexact=city).count()
    if count < 3:
        msg = f'Se puede registrar {3 - count} veces más esta ciudad.'
    else:
        msg = "No se puede registrar más veces esta ciudad."
    return render(request, 'proof/filter_cities_list.html', {
        'city': city,
        'count': count,
        'msg': msg,
    })


def register_all_cities(request):
    list_cities = Register.objects.select_related(
        'city').values('id', 'city', 'first_name').order_by('city')

    quantity_of_cities = list_cities.values('city').annotate(
        amount=Count('city')).order_by('-amount')
    return render(request, 'proof/cities_list.html', {
        'quantity_of_cities': quantity_of_cities
    })


class RegisterViewSet(viewsets.ModelViewSet):

    queryset = Register.objects.all().order_by('id')
    serializer_class = RegisterSerializer
