from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView
from django.urls import reverse_lazy
from blog.models import DataType
from blog.forms import DataTypeForm


class HomeView(TemplateView):
    template_name = 'PyDucation/home.html'

class DataTypeListView(ListView):
    model = DataType
    template_name = 'data_type_list.html'
    context_object_name = 'data_types'


class DataTypeDetailView(DetailView):
    model = DataType
    template_name = 'data_type_detail.html'
    context_object_name = 'data_type'


class DataTypeCreateView(CreateView):
    model = DataType
    form_class = DataTypeForm
    template_name = 'data_types/data_type_create.html'
    success_url = reverse_lazy('data_types:list')


class DataTypeUpdateView(UpdateView):
    model = DataType
    form_class = DataTypeForm
    template_name = 'data_type_update.html'
    context_object_name = 'data_type'
    success_url = reverse_lazy('data_types:list')


class DataTypeDeleteView(DeleteView):
    model = DataType
    template_name = 'data_type_delete.html'
    context_object_name = 'data_type'
    success_url = reverse_lazy('data_types:list')
