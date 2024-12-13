from django.urls import path
from .views import PagesListView, PageDetailsView, PagesCreate, PagesUpdate, PagesDelete

pages_patterns = ([
    path('', PagesListView.as_view(), name='pages'),
    path('<int:pk>/<slug:slug>/', PageDetailsView.as_view(), name='page'),
    path('create/', PagesCreate.as_view(), name='create' ),
    path('update/<int:pk>', PagesUpdate.as_view(), name='update' ),
    path('delete/<int:pk>', PagesDelete.as_view(), name='delete' )
], 'pages')