from re import template
from django.views.generic import TemplateView
from django.urls import path
from .views import modelEditDetailView,AddBookView,Genre,newPage,PostPreLoadView,SinglePostView,modelDetailView,IndexView
app_name = 'cbv'
urlpatterns = [
    path('', IndexView.as_view(template_name='home.html',
                                  extra_context={'title': 'This is custom context'}), name='home'),
    path('add/',AddBookView.as_view(),name='add'),

    # path('c/<slug:genre>', Genre.as_view(), name='genre'),
    # path('new',newPage.as_view(),name = 'newPage'),
    path('<slug:pk>',modelDetailView.as_view(),name = 'detail_views'),
    path('<slug:pk>/edit',modelEditDetailView.as_view(),name = 'Editdetail'),

    # path('page3/<int:pk>',PostPreLoadView.as_view(),name = 'page3'),
    # path('page4/<int:pk>',SinglePostView.as_view(),name = 'page4'),
]
