""" URL for mobile"""
from django.urls import path,include
from .import views
from .views import SearchResultsView

urlpatterns = [
    
    path('', views.index, name='index'),
    path('telephones/', views.telephones, name='telephones'),
    path('new_record/', views.new_record, name='new_record'),
    path('edit_record/<int:mobil_id>/', views.edit_record, name='edit_record'),
    path('search/', SearchResultsView.as_view(), name='search_results'),
    path('delete_record/<int:mobil_id>/',views.delete_record, name='delete_record'),
    
]
