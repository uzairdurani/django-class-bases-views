from django.views.generic import TemplateView
from django.urls import path
from .views import newPage

urlpatterns = [
    path('', TemplateView.as_view(template_name='home.html',
                                  extra_context={'title': 'This is custom context'}), name='home'),
    path('new',newPage.as_view(),name = 'newPage')
]
