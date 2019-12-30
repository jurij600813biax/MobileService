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
    path('details_new_record/', views.details_new_record, name= 'details_new_record'),
    path('details_search', views.details_search, name= 'details_search'),
    path('details_edit/<int:detail_id>/', views.details_edit, name= 'details_edit'),
    path('details_delete/<int:detail_id>/', views.details_delete, name= 'details_delete'),
    path('handbook/', views.handbook, name= 'handbook'),
    path('handbook_new_record/', views.handbook_new_record, name= 'handbook_new_record'),
    path('handbook_search/', views.handbook_search, name= 'handbook_search'),
    path('handbook_edit/<int:handbook_id>/', views.handbook_edit, name= 'handbook_edit'),
    path('handbook_delete/<int:handbook_id>/',views.handbook_delete, name= 'handbook_delete'),
    path('settings/', views.settings, name= 'settings'),
]
