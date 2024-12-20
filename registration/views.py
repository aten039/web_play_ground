from .forms import UserCreationFormWithEmail, ProfileForm, EmailForm
from django.views.generic import CreateView
from django.views.generic.edit import UpdateView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy, reverse
from django import forms 
from .models import Profile

# Create your views here.

class SignUpView(CreateView):
    form_class = UserCreationFormWithEmail
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

    def get_success_url(self):
        return reverse('login') + '?register'
    
    def get_form(self, form_class = None):
        form = super(SignUpView, self).get_form()
        
        form.fields['username'].widget = forms.TextInput(attrs={"class": "form-control mb-2", "placeholder": "Nombre de usuario"})
        form.fields['email'].widget = forms.EmailInput(attrs={"class": "form-control mb-2", "placeholder": "E-mail"})
        form.fields['password1'].widget = forms.PasswordInput(attrs={"class": "form-control mb-2", "placeholder": "contraseña"})
        form.fields['password2'].widget = forms.PasswordInput(attrs={"class": "form-control mb-2", "placeholder": "confirma tu contraseña"})

        return form

@method_decorator(login_required, name='dispatch')
class ProfileUpdate(UpdateView):
    
    success_url = reverse_lazy('profile')
    template_name = 'registration/profile_form.html'
    form_class = ProfileForm
    
    def get_object(self):
        profile, created = Profile.objects.get_or_create(user=self.request.user)
        return profile
    
class ProfileEmail(UpdateView):
    success_url = reverse_lazy('profile')
    template_name = 'registration/profile_email_form.html'
    form_class = EmailForm
    
    def get_object(self):
        return self.request.user
    
    def get_form(self, form_class = None):
        form = super(ProfileEmail, self).get_form()
        form.fields['email'].widget = forms.EmailInput(attrs={"class": "form-control mb-2", "placeholder": "E-mail"})
        return form