from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.admin.views.decorators import staff_member_required
from django.utils.decorators import method_decorator
from django.urls import reverse_lazy

from .models import Page
from .form import PageForm

# Create your views here.

class PagesListView(ListView):
    model= Page
    template_name= 'pages/pages.html'

class PageDetailsView(DetailView):
    model = Page
    template_name = 'pages/page.html'

@method_decorator(staff_member_required, 'dispatch')
class PagesCreate(CreateView):
    model= Page 
    form_class = PageForm
    template_name = 'pages/page_form.html'
    success_url = reverse_lazy('pages:pages')
    
@method_decorator(staff_member_required, 'dispatch')
class PagesUpdate(UpdateView):
    model = Page
    form_class = PageForm
    template_name = 'pages/page_update_form.html'
    def get_success_url(self):
        return reverse_lazy('pages:update', args =[ self.object.id]) + '?ok'
    
@method_decorator(staff_member_required, 'dispatch')
class PagesDelete(DeleteView):
    model = Page 
    success_url = reverse_lazy('pages:pages')
   