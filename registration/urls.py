from django.urls import path
from .views import SignUpView, ProfileUpdate, ProfileEmail

urlpatterns = [
    path('signup/', SignUpView.as_view() , name='signup' ),
    path('profile/', ProfileUpdate.as_view() , name='profile' ),
    path('profile/email', ProfileEmail.as_view() , name='profile_email' )
]