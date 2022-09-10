from django.urls import path, include
from .views import StartupListView, StartupCreateView

urlpatterns = [
    path ('', StartupListView.as_view(), name = 'home'),
    path ('portfolios/new/', StartupCreateView.as_view(), name ='create'),
]