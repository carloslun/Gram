from django.shortcuts import render, redirect
from django.http import HttpResponse
from datetime import datetime
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import *
from posts.forms import PostForm
from posts.models import Post

from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse, reverse_lazy


class FeedListView(LoginRequiredMixin, ListView):
    """
    Return all Object => 'posts'
    """
    context_object_name = 'posts'
    model = Post
    # Esto limita el número de objetos por página y agrega un paginator y page_obj al context. Para permitir que sus usuarios naveguen entre páginas, agregue enlaces a la página siguiente y anterior, en su plantilla de esta manera:
    paginate_by = 2
    ordering = ('-created')
    template_name = 'post/feed.html'


class PostDetailView(LoginRequiredMixin, DetailView):
    """
    Definicion de cada post
    """
    context_object_name = 'post'
    model = Post
    template_name = 'post/post_detail.html'


class PostCreateView(LoginRequiredMixin, CreateView): 
    """
    create a new post
    """
    template_name = 'post/new.html'
    form_class = PostForm
    success_url = reverse_lazy('posts:feed')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["user"] = self.request.user
        context["profile"] = self.request.user.profile
        return context
    

