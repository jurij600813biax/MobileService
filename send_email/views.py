from django.shortcuts import render
from django.http import HttpResponseRedirect
import django
from django.conf import settings
from django.core.mail import send_mail
from django.urls import reverse
from .models import Post, Settings_common
from .forms import PostForm,SettingsForm
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from mobile.models import Mobil

def index(request,mobil_id,message_id):
    message_send = Post.objects.filter(owner=request.user).get(id=message_id)
    mobil_send = Mobil.objects.filter(owner=request.user).get(id=mobil_id)
    send_mail('test',message_send.text_message,"Jurij",[mobil_send.email_client])
    context={'mobil_send':mobil_send,'message_send':message_send,'mobil_id':mobil_id,'message_id': message_id}
    return render(request, 'send_email/index.html',context)

def success(request):
    email = request.POST.get('email', '')
    f=open('send_email/letter.txt','r')
 #   data = """
#Hello!
#Первое сообщение из моей программы.

#    """
    data=f.read()
    send_mail('Welcome!', data, "Yasoob",
              [email], fail_silently=False)
    f.close()
    return render(request, 'send_email/success.html')

def settings_common(request):
    set_individuals = Settings_common.objects.filter(owner=request.user)
    context = {'set_individuals': set_individuals}
    return render(request, 'send_email/settings_common.html', context)

def settings_common_new(request):
    if request.method != 'POST':
        form = SettingsForm()
    else:
        form = SettingsForm(request.POST)
        if form.is_valid():
            settings = form.save(commit=False)
            settings.owner = request.user
            print('OK ?')
            settings.save()
            return HttpResponseRedirect(reverse('send_email:settings_common'))
    context = {'form': form}
    return render(request, 'send_email/settings_common_new.html', context)

def messages_new_record(request):
    if request.method != 'POST':
        form = PostForm()
    else:
        form = PostForm(request.POST)
        if form.is_valid():
            message_new = form.save(commit=False)
            message_new.owner = request.user
            message_new.save()
            return HttpResponseRedirect(reverse('send_email:messages'))
    context = {'form': form}
    return render(request, 'send_email/messages_new_record.html', context)

def messages(request):
    messages = Post.objects.filter(owner=request.user).order_by('post_message','text_message')
    context = {'messages': messages}
    return render(request, 'send_email/messages.html', context)

def messages_mobil(request,mobil_id):
    messages = Post.objects.filter(owner=request.user).order_by('post_message','text_message')
    context = {'messages': messages,'mobil_id':mobil_id}
    print('messages_mobil')
    print(mobil_id)
    return render(request, 'send_email/messages.html', context)

def messages_edit(request,message_id):
    message = Post.objects.filter(owner=request.user).get(id=message_id)
    if request.method != 'POST':
        form = PostForm(instance=message)
    else:
        form = PostForm(instance=message, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('send_email:messages'))
    context = {'form': form, 'message': message}
    return render(request, 'send_email/messages_edit.html', context)

def messages_delete(request, message_id):
    message = Post.objects.filter(owner=request.user).get(id=message_id)
    if request.method != 'POST':
        form = PostForm(instance=message)
    else:
        Post.objects.filter(id=message_id).delete()
        return HttpResponseRedirect(reverse('send_email:messages'))
    context = {'form': form, 'message': message}
    return render(request, 'send_email/messages_delete.html', context)

def messages_search(request):
    query = request.GET.get('q')
    if query:
        eto_s = Post.objects.filter(owner=request.user).order_by('post_message','text_message')
        object_list = eto_s.filter(
            Q(post_message__icontains=query) | Q(text_message__icontains=query))
        context = {'object_list': object_list}
    else:
        context = {'object_list': []}
    return render(request, 'send_email/messages_search.html', context)