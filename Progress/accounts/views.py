from django.shortcuts import render
from django.contrib.auth import login, logout, authenticate
from django.views.generic import CreateView, DetailView, ListView, UpdateView
from accounts.models import User
from accounts.forms import NewUserForm, LoginUserForm
from typing import Any
from django.contrib.auth.views import LoginView
from django.shortcuts import redirect
from django.urls import reverse, reverse_lazy
from django.http import HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

def logout_view(request):
    logout(request)
    return redirect('tests:test_page')


def UserLogin(request):
    if request.method == 'POST':
        form = LoginUserForm(request.POST)
        current_user = authenticate(request, 
                                    username=form['username'].value(),
                                    password=form['password'].value())
        if current_user:
            login(request, current_user)
    
        return redirect(reverse('tests:test_page'))
    

class UserRegisterView(CreateView):
    model = User
    template_name = 'accounts/sign_up.html'
    form_class = NewUserForm

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect(reverse('tests:test_page'))
    
    # def get_success_url(self):
    #     next_url = self.request.GET.get('next')
    #     if not next_url:
    #         next_url = self.request.POST.get('next')
    #     if not next_url:
    #         next_url = reverse('tests:test_page')
    #     return next_url