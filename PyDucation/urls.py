"""PyDucation URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
"""PyDucation URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path, include
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.decorators import login_required
from blog.views import (HomeView,
                        PyducationView,
                        DataTypeListView, 
                        DataTypeCreateView, 
                        DataTypeDetailView, 
                        DataTypeUpdateView, 
                        DataTypeDeleteView,
                        SignUpView,
                        MathOperatorListView,
                        MathOperatorCreateView,
                        MathOperatorUpdateView,
                        MathOperatorDeleteView,
                        FunctionListView,
                        FunctionCreateView,
                        FunctionDetailView,
                        FunctionUpdateView,
                        FunctionDeleteView,
                        PracticeExerciseListView, 
                        PracticeExerciseCreateView, 
                        PracticeExerciseDetailView, 
                        PracticeExerciseUpdateView, 
                        PracticeExerciseDeleteView,
                        )
from django.contrib import admin


urlpatterns = [
    path('admin/', admin.site.urls),

    # Vista para la página de inicio
    path('', HomeView.as_view(), name='home'),

    # Vista para la página de pyducation
    path('pyducation/', PyducationView.as_view(), name='pyducation'),

    # URLs de autenticación de Django
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/signup/', SignUpView.as_view(), name='signup'),
    path('accounts/login/', LoginView.as_view(), name='login'),
    path('register/', SignUpView.as_view(), name='register'),

    # URL específica para cierre de sesión de usuarios
    path('accounts/logout/', LogoutView.as_view(template_name='registration/logout.html'), name='logout'),

    # URLs del CRUD de DataType
    path('data_list/', DataTypeListView.as_view(), name='data_type_list'),
    path('data_types/create/', DataTypeCreateView.as_view(), name='data_type_create'),
    path('data_types/<int:pk>/', DataTypeDetailView.as_view(), name='data_type_detail'),
    path('data_types/<int:pk>/update/', DataTypeUpdateView.as_view(), name='data_type_update'),
    path('data_types/<int:pk>/delete/', DataTypeDeleteView.as_view(), name='data_type_delete'),

    # URLs del CRUD de MathOperator 
    path('math_operators/', MathOperatorListView.as_view(), name='math_operator_list'),
    path('math_operators/create/', MathOperatorCreateView.as_view(), name='math_operator_create'),
    path('math-operators/<int:pk>/update/', MathOperatorUpdateView.as_view(), name='math_operator_update'),
    path('math-operators/<int:pk>/delete/', MathOperatorDeleteView.as_view(), name='math_operator_delete'),

    # URLs del CRUD de MathOperator Function
    path('functions_list/', FunctionListView.as_view(), name='function_list'),
    path('functions/create/', FunctionCreateView.as_view(), name='function_create'),
    path('functions/<int:pk>/', FunctionDetailView.as_view(), name='function_detail'),
    path('functions/<int:pk>/update/', FunctionUpdateView.as_view(), name='function_update'),
    path('functions/<int:pk>/delete/', FunctionDeleteView.as_view(), name='function_delete'),
    

    # URLs del CRUD de practice_exercises Function
    path('practice_exercise_list', PracticeExerciseListView.as_view(), name='practice_exercise_list'),
    path('practice_exercise/create/', PracticeExerciseCreateView.as_view(), name='practice_exercise_create'),
    path('practice_exercise/<int:pk>/', PracticeExerciseDetailView.as_view(), name='practice_exercise_detail'),
    path('practice_exercise/<int:pk>/update/', PracticeExerciseUpdateView.as_view(), name='practice_exercise_update'),
    path('practice_exercise/<int:pk>/delete/', PracticeExerciseDeleteView.as_view(), name='practice_exercise_delete'),
]