from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from mobile.models import Mobil
from .models import Price_list,Details
from .forms import Price_listForm, DetailsForm
from django.db.models import Q
from django.contrib.auth.decorators import login_required

def logout_view(request):
    """Завершает сеанс работы с приложением."""
    logout(request)
    return HttpResponseRedirect(reverse('mobile:index'))

def register(request):
    """Регистрация"""
    if request.method != 'POST' :
        form = UserCreationForm()
    else:
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            new_user = form.save()
            authenticated_user = authenticate(username=new_user.username,
            password=request.POST['password1'])
            login(request, authenticated_user)
            return HttpResponseRedirect(reverse('mobile:index'))
    context = {'form': form}
    return render(request, 'users/register.html', context)

@login_required
def individual(request):
    """Индивидуальные настройки"""
    mobils = Mobil.objects.all()
    context = {'mobils':mobils }
    return render(request, 'users/individual.html',context)

@login_required
def service_prices(request):
    prices = Price_list.objects.filter(owner=request.user)
    context = {'prices': prices}
    return render(request, 'users/service_prices.html', context)

@login_required
def service_new_record(request):
    if request.method != 'POST':
        form = Price_listForm()
    else:
        form = Price_listForm(request.POST)
        if form.is_valid():
            service_new = form.save(commit=False)
            service_new.owner = request.user
            service_new.save()
            return HttpResponseRedirect(reverse('users:service_prices'))

    context = {'form': form}
    return render(request, 'users/service_new_record.html', context)

@login_required
def service_search(request):
    query = request.GET.get('q')
    if query:
        eto_s = Price_list.objects.filter(owner=request.user)
        object_list =eto_s.filter(
            Q(user_model__exact=query) | Q(user_model_1__exact=query) )
        context = {'object_list': object_list}
    else:
        context = {'object_list': []}
    return render(request, 'users/service_search.html', context)

@login_required
def service_edit(request,price_id):
    price = Price_list.objects.filter(owner=request.user).get(id=price_id)
    if request.method != 'POST':
        form = Price_listForm(instance=price)
    else:
        form = Price_listForm(instance=price, data=request.POST)
        if form.is_valid():
            print("IsValid")
            form.save()
            return HttpResponseRedirect(reverse('users:service_prices'))
    context = {'form': form, 'price': price}
    return render(request, 'users/service_edit.html', context)

@login_required
def service_delete(request,price_id):
    price = Price_list.objects.filter(owner=request.user).get(id=price_id)
    if request.method != 'POST':
        form = Price_listForm(instance=price)
    else:
        Price_list.objects.filter(id=price_id).delete()
        return HttpResponseRedirect(reverse('users:service_prices'))
    context = {'form': form, 'price': price}
    return render(request, 'users/service_delete.html', context)

@login_required
def details(request):
    details = Details.objects.filter(owner=request.user)
    context = {'details': details}
    return render(request, 'users/details.html', context)

@login_required
def details_new_record(request):
    if request.method != 'POST':
        form = DetailsForm()
    else:
        form = DetailsForm(request.POST)
        if form.is_valid():
            detail_new = form.save(commit=False)
            detail_new.owner = request.user
            detail_new.save()
            return HttpResponseRedirect(reverse('users:details'))
    context = {'form': form}
    return render(request, 'users/details_new_record.html', context)

@login_required
def details_search(request):
    query = request.GET.get('q')
    if query:
        eto_s = Details.objects.filter(owner=request.user)
        object_list = eto_s.filter(
            Q(user_model__exact=query) | Q(user_model_1__exact=query))
        context = {'object_list': object_list}
    else:
        context = {'object_list': []}
    return render(request, 'users/details_search.html', context)

@login_required
def details_edit(request,detail_id):
    detail = Details.objects.filter(owner=request.user).get(id=detail_id)
    if request.method != 'POST':
        form = DetailsForm(instance=detail)
    else:
        form = DetailsForm(instance=detail, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('users:details'))
    context = {'form': form, 'detail': detail}
    return render(request, 'users/details_edit.html', context)

@login_required
def details_delete(request,detail_id):
    detail = Details.objects.filter(owner=request.user).get(id=detail_id)
    if request.method != 'POST':
        form = DetailsForm(instance=detail)
    else:
        Details.objects.filter(id=detail_id).delete()
        return HttpResponseRedirect(reverse('users:details'))
    context = {'form': form, 'detail': detail}
    return render(request, 'users/details_delete.html', context)

@login_required
def handbook(request):
    return render(request, 'users/handbook.html')

@login_required
def settings(request):
    return render(request, 'users/settings.html')





