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
                        ProfileView,
                        MathOperatorListView,
                        MathOperatorCreateView,
                        MathOperatorUpdateView,
                        MathOperatorDeleteView,
                        )
from django.contrib import admin


urlpatterns = [
    # Vista para la página de inicio
    path('', HomeView.as_view(), name='home'),

    # Vista para la página de pyducation
    path('pyducation/', PyducationView.as_view(), name='pyducation'),


    # URLs del CRUD de DataType
    path('data_list/', DataTypeListView.as_view(), name='data_type_list'),
    path('data_types/create/', DataTypeCreateView.as_view(), name='data_type_create'),
    path('data_types/<int:pk>/', DataTypeDetailView.as_view(), name='data_type_detail'),
    path('data_types/<int:pk>/update/', DataTypeUpdateView.as_view(), name='data_type_update'),
    path('data_types/<int:pk>/delete/', DataTypeDeleteView.as_view(), name='data_type_delete'),

    # URL específica para cierre de sesión de usuarios
    path('accounts/logout/', LogoutView.as_view(template_name='registration/logout.html'), name='logout'),

    # URLs de autenticación de Django
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/signup/', SignUpView.as_view(), name='signup'),
    path('accounts/login/', LoginView.as_view(), name='login'),
    path('register/', SignUpView.as_view(), name='register'),
    path('profile/', ProfileView.as_view(), name='profile'),


    path('math_operators/', MathOperatorListView.as_view(), name='math_operator_list'),
    path('math_operators/create/', MathOperatorCreateView.as_view(), name='math_operator_create'),
    path('math-operators/<int:pk>/update/', MathOperatorUpdateView.as_view(), name='math_operator_update'),
    path('math-operators/<int:pk>/delete/', MathOperatorDeleteView.as_view(), name='math_operator_delete'),
]
