from .forms import UserCreationFormWithEmail
from django.views.generic import CreateView
from django.urls import reverse_lazy, reverse
from django import forms 

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

