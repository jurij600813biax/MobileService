from django.urls import path,include
from django.contrib.auth.views import LoginView
from .import views
urlpatterns=[
    path('login/', LoginView.as_view(template_name='users/login.html'),
        name='login'),
    path('register/', views.register, name='register'),
    path('logout/', views.logout_view, name='logout'),
    path('individual/', views.individual, name='individual'),
    path('service_prices/', views.service_prices, name='service_prices'),
    path('service_new_record/', views.service_new_record, name='service_new_record'),
    path('service_search/', views.service_search, name='service_search'),
    path('service_edit/<int:price_id>/', views.service_edit, name = 'service_edit'),
    path('service_delete/<int:price_id>/', views.service_delete, name= 'service_delete'),
    path('details/', views.details, name= 'details'),
    path('handbook/', views.handbook, name= 'handbook'),
    path('settings/', views.settings, name= 'settings'),
]
