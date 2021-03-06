from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.http import HttpResponseRedirect, Http404
from .models import Mobil
from send_email.models import Settings_common
from .forms import MobilForm,EditForm
from django.views.generic import ListView
from django.db.models import Q
from django.db.models import Max

def index(request):
    """home page"""
    return render(request, 'mobile/index.html')

@login_required
def telephones(request):
    mobils = Mobil.objects.filter(owner=request.user).order_by('-number_reg')
    context = {'mobils': mobils}
    return render(request, 'mobile/telephones.html', context)

@login_required
def new_record(request):
    if request.method != 'POST':
        form = MobilForm()
    else:
        form = MobilForm(request.POST)
        if form.is_valid():
            nform=form.save(commit=False)
            own_list = Mobil.objects.filter(owner=request.user)
            set_1 = Settings_common.objects.filter(owner=request.user).first()
            max_num = own_list.aggregate(Max('number_reg'))
            if not own_list:
                max_num['number_reg__max']=set_1.number_reg_start-1
            next_number_reg = max_num['number_reg__max']+1
            if next_number_reg > 99999:
                next_number_reg = 0
            nform.number_reg = str(next_number_reg)
            alen_1 = set_1.number_reg_letter + " "
            alen = len(nform.number_reg)
            while alen < 5:
                alen_1 += '0'
                alen +=1
            nform.complex_number_reg = alen_1 + str(next_number_reg)
            nform.owner = request.user
            nform.save()
            return HttpResponseRedirect(reverse('mobile:telephones'))
    context = {'form': form}
    return render(request, 'mobile/new_record.html', context)

@login_required
def edit_record(request,mobil_id):
    mobil=Mobil.objects.filter(owner=request.user).get(id=mobil_id)
    set_1 = Settings_common.objects.filter(owner=request.user).first()
    if request.method != 'POST':
        form = EditForm(instance=mobil)
    else:
        form = EditForm(instance=mobil, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('mobile:telephones'))
    context = {'form': form,'mobil':mobil,'set_1':set_1}
    return render(request, 'mobile/edit_record.html', context)

@login_required
def delete_record(request,mobil_id):
    mobil=Mobil.objects.get(id=mobil_id)
    if request.method !='POST':
        form = EditForm(instance=mobil)
    else:
        Mobil.objects.filter(id=mobil_id).delete()
        return HttpResponseRedirect(reverse('mobile:telephones'))
    context = {'form': form, 'mobil': mobil}
    return render( request, 'mobile/delete_record.html',context)

@login_required
def search_results(request):
    query = request.GET.get('q')
    if query:
        eto = Mobil.objects.filter(owner=request.user)
        object_list =eto.filter(
            Q(model_tel__icontains=query) | Q(imei__exact=query) | Q(number_tel__exact=query) |
            Q(model_1_tel__icontains=query) | Q(number_sticker__exact=query) | Q(comment__icontains=query)
            | Q(number_reg__icontains=query) | Q(defect_tel__icontains=query) | Q(defect__icontains=query)
            | Q(status__icontains=query)
                ).order_by('-number_reg')
        context = {'object_list': object_list}
    else:
        context = {'object_list': []}
    return render(request, 'mobile/search_results.html', context)


            

    

        
        
    
