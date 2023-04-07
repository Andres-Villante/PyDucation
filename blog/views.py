from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import UserCreationForm
from blog.models import DataType
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from django.utils.decorators import method_decorator



class HomeView(TemplateView):
    template_name = 'PyDucation/home.html'

# Vista para listar los elementos del CRUD
class DataTypeListView(LoginRequiredMixin, ListView):
    template_name = 'data_types/data_type_list.html'
    model = DataType
    context_object_name = 'data_types'

# Vista para crear un elemento del CRUD
class DataTypeCreateView(LoginRequiredMixin, CreateView):
    template_name = 'data_types/data_type_create.html'
    model = DataType
    fields = ['name', 'description']
    success_url = reverse_lazy('data_type_list')

# Vista para ver los detalles de un elemento del CRUD
class DataTypeDetailView(LoginRequiredMixin, DetailView):
    template_name = 'data_types/data_type_detail.html'
    model = DataType
    context_object_name = 'data_type'

# Vista para actualizar un elemento del CRUD
class DataTypeUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'data_types/data_type_update.html'
    model = DataType
    fields = ['name', 'description']
    context_object_name = 'data_type'
    success_url = reverse_lazy('data_type_list')

# Vista para eliminar un elemento del CRUD
class DataTypeDeleteView(LoginRequiredMixin, DeleteView):
    template_name = 'data_types/data_type_delete.html'
    model = DataType
    context_object_name = 'data_type'
    success_url = reverse_lazy('data_type_list')

# Vista para la página de registro de usuarios
class SignUpView(CreateView):
    form_class = UserCreationForm
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('login')

# Vista para la página de inicio de sesión de usuarios
class LoginView(LoginView):
    template_name = 'registration/login.html'

    # Si el usuario se ha autenticado correctamente, se redirige a la página de inicio del CRUD
    def get_success_url(self):
        return reverse_lazy('data_type_list')

# Vista para la página de cierre de sesión de usuarios
class LogoutView(LogoutView):
    template_name = 'registration/logout.html'


class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'registration/profile.html'