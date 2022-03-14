from django.shortcuts import redirect, render
from .models import File

from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.urls import reverse_lazy

from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login


class CustomLoginView(LoginView):
    template_name = 'base/login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('files')

class RegisterPage(FormView):
    template_name = 'base/register.html'
    form_class = UserCreationForm
    redirect_authenticated_user = True
    success_url =  reverse_lazy('files')

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(RegisterPage, self).form_valid(form)

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('files')
        return super(RegisterPage, self).get(*args, **kwargs)

class FileList(LoginRequiredMixin, ListView):
    model = File
    context_object_name = 'files'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['files'] = context['files'].filter(user=self.request.user)
        return context

class FileDetail(DetailView):
    model = File
    context_object_name = 'file'
    
class FileCreate(LoginRequiredMixin,CreateView):
    model = File
    fields = ['title', 'body']
    success_url = reverse_lazy('files')
    template_name= 'base/create.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(FileCreate, self).form_valid(form)

class FileUpdate(LoginRequiredMixin, UpdateView):
    model = File
    fields = ['title', 'body']
    success_url = reverse_lazy('files')
    template_name= 'base/create.html'

class FileDelete(LoginRequiredMixin, DeleteView):
    model = File
    context_object_name = 'file'
    success_url = reverse_lazy('files')



@login_required 
def about(request):
    return render(request, 'base/about.html')
