from pyexpat import model
from django.shortcuts import render
from django.views.generic.base import TemplateView,RedirectView
from .models import student,Post
from django.shortcuts import get_object_or_404
from django.db.models import F
from django.views.generic import DetailView
# Create your views here.
class newPage(TemplateView):
    template_name = 'newPage.html'
    def get_context_data(self, **kwargs):
      context =  super().get_context_data(**kwargs)
      context['posts']  = Post.objects.get(id = 1)
      context['data'] = 'Name From Student Model'
      return context


class PostPreLoadView(RedirectView):
  pattern_name = 'cbv:page4'
  def get_redirect_url(self, *args, **kwargs):
    # post = get_object_or_404(id = kwargs['pk'])
    post = Post.objects.filter(id = kwargs['pk'])
    post.update(count = F('count') + 1)
    return super().get_redirect_url(*args, **kwargs)
    
class SinglePostView(TemplateView):
    template_name = 'page4.html'
    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        context['posts'] = get_object_or_404(Post, id = self.kwargs.get('pk'))
        return context


class modelDetailView(DetailView):
  model = student
  template_name = 'student_detail.html'
  