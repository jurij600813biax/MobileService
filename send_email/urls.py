from django.urls import path,include
from .import views

urlpatterns=[
    path('', views.index, name='index'),
    path('success', views.success, name='success'),
    path('messages_new_record', views.messages_new_record, name='messages_new_record'),
    path('messages', views.messages, name= 'messages'),
    path('messages_edit/<int:message_id>/', views.messages_edit, name= 'messages_edit'),
    path('messages_delete/<int:message_id>/', views.messages_delete, name= 'messages_delete'),
    path('messages_search', views.messages_search, name='messages_search'),
    ]
