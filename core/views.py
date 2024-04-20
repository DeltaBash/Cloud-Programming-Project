from .models import Core
from django.views.generic import TemplateView
from django.views.generic import ListView, DetailView, UpdateView, DeleteView, CreateView
from django.urls import reverse_lazy
import random
from django.shortcuts import render   
from content.news_lib.news_lib.news import get_random_headline



class IndexView(ListView):
    model = Core
    template_name = 'core/index.html'
    context_object_name = 'index'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['random_headline'] = get_random_headline()
        return context


class SingleView(DetailView):
    model = Core
    template_name = 'core/single.html'
    context_object_name = 'post'


class PostsView(ListView):
    model = Core
    template_name = 'core/posts.html'
    context_object_name = 'post_list'


class AddView(CreateView):
    model = Core
    template_name = 'core/add.html'
    fields = '__all__'
    success_url = reverse_lazy('core:posts')


class EditView(UpdateView):
    model = Core
    template_name = 'core/edit.html'
    fields = '__all__'
    pk_url_kwarg = 'pk'
    success_url = reverse_lazy('core:posts')


class Delete(DeleteView):
    model = Core
    pk_url_kwarg = 'pk'
    success_url = reverse_lazy('core:posts')
    template_name = 'core/confirm-delete.html'
    
    