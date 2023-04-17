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

from django.conf.urls.static import static, settings
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
                        ProfileCreateView,
                        ProfileDetailView,
                        ProfileUpdateView,
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
                        PracticeExerciseEasyView,
                        PracticeExerciseIntermediateView,
                        PracticeExerciseHardView,
                        PostListView,
                        PostCreateView,
                        PostDetailView,
                        ChatView,
                        PostResponseView,
                        About,
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

    # URLs de perfil
    path('profile/create/', ProfileCreateView.as_view(), name='profile_create'),
    path('profile/<int:pk>/', ProfileDetailView.as_view(), name='profile_detail'),
    path('profile/<int:pk>/update/', ProfileUpdateView.as_view(), name='profile_update'),


    # URL específica para cierre de sesión de usuarios
    path('custom_logout/', LogoutView.as_view(template_name='registration/logout.html'), name='logout'),


    # URLs del CRUD de DataType
    path('data-types/', DataTypeListView.as_view(), name='data_type_list'),
    path('data-types/create/', DataTypeCreateView.as_view(), name='data_type_create'),
    path('data-types/<int:pk>/', DataTypeDetailView.as_view(), name='data_type_detail'),
    path('data-types/<int:pk>/update/', DataTypeUpdateView.as_view(), name='data_type_update'),
    path('data-types/<int:pk>/delete/', DataTypeDeleteView.as_view(), name='data_type_delete'),
    
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
    

    # URLs de practice_exercises 
    path('ejercicios/', PracticeExerciseListView.as_view(), name='exercise_list'),
    path('easy/exercises/', PracticeExerciseEasyView.as_view(), name='easy_exercise_list'),
    path('intermediate_/exercises/', PracticeExerciseIntermediateView.as_view(), name='intermediate_exercise_list'),
    path('difficult/exercises/', PracticeExerciseHardView.as_view(), name='difficult_exercise_list'),


    path('post_list/', PostListView.as_view(), name='post_list'),
    path('create/', PostCreateView.as_view(), name='post_create'),
    path('<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    path('<int:pk>/response/', PostResponseView.as_view(), name='post_response'),
    path('chat/', ChatView.as_view(), name='chat'),

    
    path('about/', About, name='about'),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


