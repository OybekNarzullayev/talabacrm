from django.urls import path
from .views import *

urlpatterns = [
    path('',StundetListView.as_view(), name='base'),
    path('s_create',StudentCreateView.as_view(),name = 's_create'),
    path('s_delete/<int:pk>/',DeleteView.as_view(),name='s_delete'),
    path('s_update/<int:pk>/',UpdateView.as_view(),name='update'),
    path('s_detail/<int:pk>/',DetailView.as_view(),name='s_detail')
]