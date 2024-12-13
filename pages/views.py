from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Page

# Create your views here.

class PagesListView(ListView):
    model= Page
    template_name= 'pages/pages.html'

class PageDetailsView(DetailView):
    model = Page
    template_name = 'pages/page.html'

class PagesCreate(CreateView):
    model= Page 
    template_name = 'pages/page_form.html'
    fields= ['title', 'content', 'order']
    success_url = reverse_lazy('pages:pages')

class PagesUpdate(UpdateView):
    model = Page
    fields = ['title', 'content', 'order']
    template_name = 'pages/page_update_form.html'
    
    def get_success_url(self):
        return reverse_lazy('pages:update', args =[ self.object.id]) + '?ok'
    
class PagesDelete(DeleteView):
    model = Page 
    success_url = reverse_lazy('pages:pages')
   