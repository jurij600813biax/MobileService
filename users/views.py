from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from mobile.models import Mobil
from .models import Price_list,Details,Details_order,Handbook
from .forms import Price_listForm, DetailsForm, Details_orderForm, HandbookForm
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
    return render(request, 'users/individual.html')

@login_required
def service_prices(request):
    prices = Price_list.objects.filter(owner=request.user).order_by('user_model','user_model_1')
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
            Q(user_model__icontains=query) | Q(user_model_1__icontains=query) )
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
    details = Details.objects.filter(owner=request.user).order_by('user_model','user_model_1')
    context = {'details': details}
    return render(request, 'users/details.html', context)

def details_order(request):
    details_order = Details_order.objects.filter(owner=request.user).order_by('user_model', 'user_model_1')
    context = {'details_order': details_order}
    return render(request, 'users/details_order.html', context)

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
def details_order_new_record(request):
    if request.method != 'POST':
        form = Details_orderForm()
    else:
        form = Details_orderForm(request.POST)
        if form.is_valid():
            detail_order_new = form.save(commit=False)
            detail_order_new.owner = request.user
            detail_order_new.save()
            return HttpResponseRedirect(reverse('users:details_order'))
    context = {'form': form}
    return render(request, 'users/details_order_new_record.html', context)


@login_required
def details_search(request):
    query = request.GET.get('q')
    if query:
        eto_s = Details.objects.filter(owner=request.user).order_by('user_model','user_model_1')
        object_list = eto_s.filter(
            Q(user_model__icontains=query) | Q(user_model_1__icontains=query) | Q(detail_visible__icontains=query))
        context = {'object_list': object_list}
    else:
        context = {'object_list': []}
    return render(request, 'users/details_search.html', context)

def details_order_search(request):
    query = request.GET.get('q')
    if query:
        eto_s = Details_order.objects.filter(owner=request.user).order_by('user_model','user_model_1')
        object_list = eto_s.filter(
            Q(user_model__icontains=query) | Q(user_model_1__icontains=query) | Q(number_tel_order__exact=query))
        context = {'object_list': object_list}
    else:
        context = {'object_list': []}
    return render(request, 'users/details_order_search.html', context)


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

def details_order_edit(request,detail_order_id):
    detail_order = Details_order.objects.filter(owner=request.user).get(id=detail_order_id)
    if request.method != 'POST':
        form = Details_orderForm(instance=detail_order)
    else:
        form = Details_orderForm(instance=detail_order, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('users:details_order'))
    context = {'form': form, 'detail_order': detail_order}
    return render(request, 'users/details_order_edit.html', context)

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

def details_order_delete(request,detail_order_id):
    detail_order = Details_order.objects.filter(owner=request.user).get(id=detail_order_id)
    if request.method != 'POST':
        form = Details_orderForm(instance=detail_order)
    else:
        Details_order.objects.filter(id=detail_order_id).delete()
        return HttpResponseRedirect(reverse('users:details_order'))
    context = {'form': form, 'detail_order': detail_order}
    return render(request, 'users/details_order_delete.html', context)

@login_required
def handbook(request):
    handbooks = Handbook.objects.filter(owner=request.user).order_by('handbook_model')
    context = {'handbooks': handbooks}
    return render(request, 'users/handbook.html',context)

@login_required
def handbook_new_record(request):
    if request.method != 'POST':
        form = HandbookForm()
    else:
        form = HandbookForm(request.POST)
        if form.is_valid():
            handbook_new = form.save(commit=False)
            handbook_new.owner = request.user
            handbook_new.save()
            return HttpResponseRedirect(reverse('users:handbook'))
    context = {'form': form}
    return render(request, 'users/handbook_new_record.html', context)

@login_required
def handbook_search(request):
    query = request.GET.get('q')
    if query:
        eto_s = Handbook.objects.filter(owner=request.user).order_by('handbook_model')
        object_list = eto_s.filter(
            Q(handbook_model__icontains=query) | Q(designation__icontains=query))
        context = {'object_list': object_list}
    else:
        context = {'object_list': []}
    return render(request, 'users/handbook_search.html', context)

@login_required
def handbook_edit(request,handbook_id):
    handbook = Handbook.objects.filter(owner=request.user).get(id=handbook_id)
    if request.method != 'POST':
        form = HandbookForm(instance=handbook)
    else:
        form = HandbookForm(instance=handbook, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('users:handbook'))
    context = {'form': form, 'handbook': handbook}
    return render(request, 'users/handbook_edit.html', context)

@login_required
def handbook_delete(request, handbook_id):
    handbook = Handbook.objects.filter(owner=request.user).get(id=handbook_id)
    if request.method != 'POST':
        form = HandbookForm(instance=handbook)
    else:
        Handbook.objects.filter(id=handbook_id).delete()
        return HttpResponseRedirect(reverse('users:handbook'))
    context = {'form': form, 'handbook': handbook}
    return render(request, 'users/handbook_delete.html', context)



@login_required
def settings(request):
    return render(request, 'users/settings.html')





