from django.urls import path
from .views import ProfileListView, ProfileDetailsView

profiles_patterns = ([
    path('', ProfileListView.as_view(), name='list' ),
    path('<username>/', ProfileDetailsView.as_view(), name='detail' ),
], 'profiles')