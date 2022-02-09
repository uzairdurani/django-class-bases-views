from re import template
from django.views.generic import TemplateView
from django.urls import path
from .views import newPage,PostPreLoadView,SinglePostView,modelDetailView
app_name = 'cbv'
urlpatterns = [
    path('', TemplateView.as_view(template_name='home.html',
                                  extra_context={'title': 'This is custom context'}), name='home'),
    path('new',newPage.as_view(),name = 'newPage'),
    path('<slug:pk>',modelDetailView.as_view(),name = 'detail_views'),
    path('page3/<int:pk>',PostPreLoadView.as_view(),name = 'page3'),
    path('page4/<int:pk>',SinglePostView.as_view(),name = 'page4'),
]
