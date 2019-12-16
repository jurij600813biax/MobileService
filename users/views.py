from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.forms import UserCreationForm
from mobile.models import Mobil
from .models import Price_list
from .forms import Price_listForm
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

 
def individual(request):
    """Индивидуальные настройки"""
    mobils = Mobil.objects.all()
    context = {'mobils':mobils }
    return render(request, 'users/individual.html',context)

def service_prices(request):
    prices = Price_list.objects.filter(owner=request.user)
    context = {'prices': prices}
    return render(request, 'users/service_prices.html', context)

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

def service_delete(request,price_id):
    price = Price_list.objects.get(id=price_id)
    if request.method != 'POST':
        form = Price_listForm(instance=price)
    else:
        Price_list.objects.filter(id=price_id).delete()
        return HttpResponseRedirect(reverse('users:service_prices'))
    context = {'form': form, 'price': price}
    return render(request, 'users/service_delete.html', context)

def details(request):
    return render(request, 'users/details.html')

def handbook(request):
    return render(request, 'users/handbook.html')

def settings(request):
    return render(request, 'users/settings.html')




