# Importaciones necesarias
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView, View
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import UserCreationForm
from blog.models import DataType, MathOperator, Function, PracticeExercise, Post, Response
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from django.utils.decorators import method_decorator
from django.contrib.auth.forms import UserChangeForm
from blog.forms import PostForm, ResponseForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.http import HttpResponseForbidden



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

    def form_valid(self, form):
        form.instance.data_type_created_by = self.request.user
        return super().form_valid(form)


# Vista para ver los detalles de un elemento del CRUD
class DataTypeDetailView(LoginRequiredMixin, DetailView):
    template_name = 'data_types/data_type_detail.html'
    model = DataType
    context_object_name = 'data_type'

class DataTypeUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    template_name = 'data_types/data_type_update.html'
    model = DataType
    fields = ['name', 'description', 'example']
    context_object_name = 'data_type'
    success_url = reverse_lazy('data_type_list')

    def test_func(self):
        obj = self.get_object()
        if obj.data_type_created_by == self.request.user:
            return True

    def handle_no_permission(self):
        return HttpResponseForbidden()


class DataTypeDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = DataType
    success_url = reverse_lazy('data_type_list')

    def test_func(self):
        obj = self.get_object()
        if obj.data_type_created_by == self.request.user:
            return True

    def handle_no_permission(self):
        return HttpResponseForbidden()


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
class MathOperatorCreateView(LoginRequiredMixin, CreateView):
    model = MathOperator
    template_name = 'math_operators/math_operator_form.html'
    fields = ['name', 'symbol', 'description', 'example']
    success_url = reverse_lazy('math_operator_list')

    def form_valid(self, form):
        form.instance.math_operator_created_by = self.request.user
        return super().form_valid(form)

# Vista para actualizar un operador matemático
class MathOperatorUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = MathOperator
    template_name = 'math_operators/math_operator_form.html'
    fields = ['name', 'symbol', 'description', 'example']
    success_url = reverse_lazy('math_operator_list')

    def test_func(self):
        obj = self.get_object()
        if obj.math_operator_created_by == self.request.user:
            return True

    def handle_no_permission(self):
        messages.warning(self.request, 'No tienes permiso para editar este tipo de datos.')
        return HttpResponseForbidden()

# Vista para eliminar un operador matemático
class MathOperatorDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = MathOperator
    template_name = 'math_operators/math_operator_delete.html'
    success_url = reverse_lazy('math_operator_list')

    def test_func(self):
        obj = self.get_object()
        if obj.math_operator_created_by == self.request.user:
            return True

    def handle_no_permission(self):
        messages.warning(self.request, 'No tienes permiso para eliminar este tipo de datos.')
        return HttpResponseForbidden()









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

    def form_valid(self, form):
        form.instance.functions_created_by = self.request.user
        return super().form_valid(form)

# Vista para ver los detalles de una funcion
class FunctionDetailView(DetailView):
    model = Function
    template_name = 'functions/function_detail.html'
    context_object_name = 'function'

# Vista para actualizar una funcion
class FunctionUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Function
    template_name = 'functions/function_form.html'
    fields = ['name', 'description', 'example']
    success_url = reverse_lazy('function_list')

    def test_func(self):
        obj = self.get_object()
        if obj.functions_created_by == self.request.user:
            return True

    def handle_no_permission(self):
        return HttpResponseForbidden()

# Vista para eliminar una funcion
class FunctionDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Function
    template_name = 'functions/function_delete.html'
    success_url = reverse_lazy('function_list')

    def test_func(self):
        obj = self.get_object()
        if obj.functions_created_by == self.request.user:
            return True
    
    def handle_no_permission(self):
        return HttpResponseForbidden()





class PracticeExerciseEasyView(TemplateView):
    template_name = 'practice_exercise/practice_exercise_easy.html'

class PracticeExerciseIntermediateView(TemplateView):
    template_name = 'practice_exercise/practice_exercise_intermediate.html'

class PracticeExerciseHardView(TemplateView):
    template_name = 'practice_exercise/practice_exercise_hard.html'

class PracticeExerciseListView(TemplateView):
    template_name = 'practice_exercise/practice_exercise_list.html'




class PostListView(View):
    def get(self, request):
        posts = Post.objects.all()
        context = {'posts': posts}
        return render(request, 'forum/post_list.html', context)

class PostCreateView(LoginRequiredMixin, View):
    login_url = reverse_lazy('login')
    form_class = PostForm
    template_name = 'forum/post_form.html'

    def get(self, request):
        form = self.form_class()
        context = {'form': form}
        return render(request, self.template_name, context)

    def post(self, request):
        form = self.form_class(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('post_list')
        context = {'form': form}
        return render(request, self.template_name, context)

class PostDetailView(View):
    def get(self, request, pk):
        post = get_object_or_404(Post, pk=pk)
        responses = Response.objects.filter(post=post)
        context = {'post': post, 'responses': responses}
        return render(request, 'forum/post_detail.html', context)

class ChatView(View):
    def get(self, request):
        context = {}
        return render(request, 'forum/chat.html', context)


class PostResponseView(LoginRequiredMixin, View):
    login_url = reverse_lazy('login')
    form_class = ResponseForm
    template_name = 'forum/post_response.html'

    def get(self, request, pk):
        post = get_object_or_404(Post, pk=pk)
        form = self.form_class()
        context = {'form': form, 'post': post}
        return render(request, self.template_name, context)

    def post(self, request, pk):
        post = get_object_or_404(Post, pk=pk)
        form = self.form_class(request.POST)
        if form.is_valid():
            response = form.save(commit=False)
            response.post = post
            response.author = request.user
            response.save()
            return redirect('post_detail', pk=post.pk)
        context = {'form': form, 'post': post}
        return render(request, self.template_name, context)