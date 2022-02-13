
from gc import get_objects
from pyexpat import model
from sre_constants import SUCCESS
from django.shortcuts import render
from django.views.generic.base import TemplateView,RedirectView
from .models import student,Post
from django.shortcuts import get_object_or_404
from django.db.models import F
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import FormView,CreateView,UpdateView
from .form import AddForm
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.auth.views import redirect_to_login
from django.shortcuts import redirect
# Create your views here.


class UserAccessMixins(PermissionRequiredMixin):
  def dispatch(self, request, *args, **kwargs) :
    if (not self.request.user.is_authenticated):
      return redirect_to_login(self.request.get_full_path(), self.get_login_url(), self.get_redirect_field_name())
    if not self.has_permission:
      return redirect('/')
    return super(UserAccessMixins,self).dispatch(request,*args,**kwargs)

class modelEditDetailView(UserAccessMixins ,UpdateView):
    raise_exception = False
    permission_required = 'CBV.schange_CBV'
    permission_denied_message = ""
    login_url = '/' 
    redirect_field_name = 'next'

    model = student
    form_class = AddForm
    template_name = 'add.html'
    success_url = '/' 
        
    
    

class AddBookView(UserAccessMixins,CreateView):
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
  