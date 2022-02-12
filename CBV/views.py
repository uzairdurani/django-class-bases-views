from pyexpat import model
from django.shortcuts import render
from django.views.generic.base import TemplateView,RedirectView
from .models import student,Post
from django.shortcuts import get_object_or_404
from django.db.models import F
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import FormView,CreateView
from .form import AddForm
# Create your views here.



class AddBookView(CreateView):
    model = student
    form_class = AddForm
    template_name = 'add.html'
    success_url = '/'


# class AddBookView(FormView):
#   template_name = 'add.html'
#   form_class = AddForm
#   success_url = '/'

#   def form_valid(self, form) :
#       form.save()
#       return super().form_valid(form)


class IndexView(ListView):
  model = student
  template_name = 'home.html'
  paginate_by = 1



class Genre(ListView):
  model = student
  template_name = 'genre.html'
  def get_queryset(self):
      return student.objects.filter(name__icontains=self.kwargs['genre'])










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
  