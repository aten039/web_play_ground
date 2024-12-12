from django.urls import path
from .views import PagesListView, PageDetailsView


urlpatterns = [
    path('', PagesListView.as_view(), name='pages'),
    path('<int:pk>/<slug:slug>/', PageDetailsView.as_view(), name='page'),
]