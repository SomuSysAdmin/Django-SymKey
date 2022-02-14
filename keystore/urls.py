from django.urls import path

from .views import CredsListView, CredsDetailView, CredsCreateView, CredsUpdateView, CredsDeleteView


urlpatterns = [
    path('', CredsListView.as_view(), name='creds-home'),
    path('creds/<int:pk>/', CredsDetailView.as_view(), name='creds-detail'),
    path('creds/add/', CredsCreateView.as_view(), name='creds-add'),
    path('creds/<int:pk>/edit', CredsUpdateView.as_view(), name='creds-edit'),
    path('creds/<int:pk>/delete', CredsDeleteView.as_view(), name='creds-delete'),
]
