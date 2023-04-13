# Importaciones necesarias
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import UserCreationForm
from blog.models import DataType, MathOperator, Function, PracticeExercise
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from django.utils.decorators import method_decorator
from django.views import View
from django.contrib.auth.forms import UserChangeForm


def about(request):
    return render(request, 'PyDucation/about.html')

"""
VISTAS DE PYDUCATION
"""

# Vista de inicio
class HomeView(TemplateView):
    template_name = 'PyDucation/home.html'

# Vista de PyDucation
class PyducationView(TemplateView):
    template_name = 'pyducation.html'

"""
CRUD de data_types
"""

# Vista para listar los elementos del CRUD
class DataTypeListView(LoginRequiredMixin, ListView):
    template_name = 'data_types/data_type_list.html'
    model = DataType
    context_object_name = 'data_types'

# Vista para crear un elemento del CRUD
class DataTypeCreateView(LoginRequiredMixin, CreateView):
    template_name = 'data_types/data_type_create.html'
    model = DataType
    fields = ['name', 'description','example']
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
    fields = ['name', 'description', 'example']
    context_object_name = 'data_type'
    success_url = reverse_lazy('data_type_list')

# Vista para eliminar un elemento del CRUD
class DataTypeDeleteView(LoginRequiredMixin, DeleteView):
    model = DataType
    success_url = reverse_lazy('data_type_list')

"""
AUTENTICACIÓN DE USUARIOS
"""

# Vista para la página de registro de usuarios
class SignUpView(CreateView):
    form_class = UserCreationForm
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('login')

# Vista para la página de inicio de sesión de usuarios
class LoginView(LoginView):
    template_name = 'registration/login.html'

# Vista para la página de cierre de sesión de usuarios
class LogoutView(LogoutView):
    template_name = 'registration/logout.html'


"""
PERFIL
"""

# Vista para el perfil del usuario


"""
CRUD de math_operators
"""

# Vista para listar los operador matemático
class MathOperatorListView(ListView):
    model = MathOperator
    template_name = 'math_operators/math_operator_list.html'
    context_object_name = 'math_operators'

# Vista para crear un operador matemático
class MathOperatorCreateView(CreateView):
    model = MathOperator
    template_name = 'math_operators/math_operator_form.html'
    fields = ['name', 'symbol', 'description', 'example']
    success_url = reverse_lazy('math_operator_list')

# Vista para actualizar un operador matemático
class MathOperatorUpdateView(UpdateView):
    model = MathOperator
    template_name = 'math_operators/math_operator_form.html'
    fields = ['name', 'symbol', 'description', 'example']
    success_url = reverse_lazy('math_operator_list')

# Vista para eliminar un operador matemático
class MathOperatorDeleteView(DeleteView):
    model = MathOperator
    template_name = 'math_operators/math_operator_delete.html'
    success_url = reverse_lazy('math_operator_list')

"""
CRUD de functions
"""

# Vista para listar las funciones
class FunctionListView(ListView):
    model = Function
    template_name = 'functions/function_list.html'
    context_object_name = 'functions'

# Vista para crear una funcion
class FunctionCreateView(CreateView):
    model = Function
    template_name = 'functions/function_form.html'
    fields = ['name', 'description', 'example']
    success_url = reverse_lazy('function_list')

# Vista para ver los detalles de una funcion
class FunctionDetailView(DetailView):
    model = Function
    template_name = 'functions/function_detail.html'
    context_object_name = 'function'

# Vista para actualizar una funcion
class FunctionUpdateView(UpdateView):
    model = Function
    template_name = 'functions/function_form.html'
    fields = ['name', 'description', 'example']
    success_url = reverse_lazy('function_list')

# Vista para eliminar una funcion
class FunctionDeleteView(DeleteView):
    model = Function
    template_name = 'functions/function_delete.html'
    success_url = reverse_lazy('function_list')





class PracticeExerciseListView(ListView):
    template_name = 'practice_exercise/practice_exercise_list.html'
    model = PracticeExercise
    context_object_name = 'exercises'


class PracticeExerciseCreateView(LoginRequiredMixin, CreateView):
    template_name = 'practice_exercise/practice_exercise_create.html'
    model = PracticeExercise
    fields = ['title', 'description', 'level']
    success_url = reverse_lazy('practice_exercise_list')


class PracticeExerciseDetailView(DetailView):
    template_name = 'practice_exercise/practice_exercise_detail.html'
    model = PracticeExercise
    context_object_name = 'exercise'


class PracticeExerciseUpdateView(UpdateView):
    template_name = 'practice_exercise/practice_exercise_update.html'
    model = PracticeExercise
    fields = ['title', 'description', 'level']
    context_object_name = 'exercise'
    success_url = reverse_lazy('practice_exercise_list')


class PracticeExerciseDeleteView(DeleteView):
    template_name = 'practice_exercise/practice_exercise_delete.html'
    model = PracticeExercise
    context_object_name = 'exercise'
    success_url = reverse_lazy('practice_exercise_list')