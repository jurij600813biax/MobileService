from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.forms import UserCreationForm
from mobile.models import Mobil


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

