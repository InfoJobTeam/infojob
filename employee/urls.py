from django.urls import path
from .views import *


app_name = 'employee'

urlpatterns = [
	path('', HomepageView.as_view(), name='employee'),
	path('<int:pk>/', CollectionDetailView.as_view(), name='cv_detail'),
    path('create/', CollectionCreate.as_view(), name='cv_create'),
    path('update/<int:pk>/', CollectionUpdate.as_view(), name='cv_update'),
    path('delete/<int:pk>/', CollectionDelete.as_view(), name='cv_delete'),


	]
