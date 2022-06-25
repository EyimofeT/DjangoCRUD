from django.shortcuts import render
from django.views import generic
from .models import Post
from django.urls import reverse_lazy

from django.views.generic.edit import CreateView
from django.views.generic.edit import DeleteView
from django.views.generic.edit import UpdateView

# Create your views here.


class PostListView(generic.ListView):
    model = Post


class PostCreateView(CreateView):
    model = Post
    fields = '__all__'
    success_url = reverse_lazy('blog: all')


class PostDetailView(generic.DetailView):
    model = Post


class PostUpdateView(UpdateView):
    model = Post
    fields = '__all__'
    success_url = reverse_lazy('blog: all')
    
class PostDeleteView(DeleteView):
    model = Post
    fields = '__all__'
    success_url = reverse_lazy('blog: all')
