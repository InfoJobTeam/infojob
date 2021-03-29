from django.urls import path
from .views import *


app_name = 'employer'

urlpatterns = [
	path('', HomepageView.as_view(), name='employer'),
	path('<int:pk>/', CompanyDetail.as_view(), name='company_detail'),
    path('create/', CompanyCreate.as_view(), name='company_create'),
    path('update/<int:pk>/', CompanyUpdate.as_view(), name='company_update'),
    path('delete/<int:pk>/', CompanyDelete.as_view(), name='company_delete'),
	]