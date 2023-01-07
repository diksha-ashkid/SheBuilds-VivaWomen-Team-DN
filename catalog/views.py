from django.shortcuts import render

from .models import ProfileDetails
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

def index(request):
    """View function for home page of site."""

    # Generate counts of some of the main objects
    num_users = ProfileDetails.objects.all().count()

    context = {
        'num_users': num_users,       
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)

from django.views import generic

class UsersList(generic.ListView):
    model = ProfileDetails
    template_name = 'catalog/user_list.html'
    context_object_name = 'user_list'

class UsersDetail(generic.DetailView):
    model = ProfileDetails 
    template_name = 'catalog/user_detail.html' 
    context_object_name = 'user'


class UsersCreate(CreateView):
    model = ProfileDetails
    fields = '__all__'
    initial = {'Birth_Date': '01/01/1918'}
    template_name = 'catalog/user_form.html'

class UsersDelete(DeleteView):
    model = ProfileDetails
    success_url = reverse_lazy('users')
    template_name = 'catalog/user_confirm_delete.html'
    context_object_name = 'user'