from django.urls import path
from .views import NastahouseListView,NastahouseCreateView,NastahouseDetailView,NastahouseUpdateView

urlpatterns = [
    path('listget/', NastahouseListView.as_view(), name='nastahouse-list'),
    path('createlist/', NastahouseCreateView.as_view(), name='nastahouse-create'),
    path('update/<int:id>/', NastahouseDetailView.as_view(), name='nastahouse-update'),
    path('delete/<int:id>/', NastahouseUpdateView.as_view(), name='nastahouse-delete'),
]