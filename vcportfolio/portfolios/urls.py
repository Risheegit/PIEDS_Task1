from django.urls import path, include
from .views import StartupListView, StartupCreateView, StartupFilter

urlpatterns = [
    path ('', StartupListView.as_view(), name = 'home'),
    path ('portfolios/new/', StartupCreateView.as_view(), name ='create'),
    path('portfolios/startup-filter/', StartupFilter.as_view(), name= 'startup-filter')
]
