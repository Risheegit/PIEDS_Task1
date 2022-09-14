"""vcportfolio URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, reverse_lazy
from django.conf import settings 
from django.views.generic.base import RedirectView
from django.conf.urls.static import static
from portfolios.views import StartupSearch, External_Redirect, StartupFilter
from portfolios import views as portfolio_views
from users import views as user_views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('admin/', RedirectView.as_view(url=reverse_lazy('admin:index')), name = 'admin'),
    path('', include('portfolios.urls')),
    path('home/', include("portfolios.urls")),
    path('portfolios/', include("portfolios.urls")),
    path('search/', StartupSearch.as_view(), name='search'),
    path('external-redirect/', External_Redirect.as_view() , name = 'external-redirect' ),
    path('startup-filter/', StartupFilter.as_view(), name ='startup-filter'),
    path ('login/', auth_views.LoginView.as_view(template_name = 'users/login.html'),name = 'login' ),
    path ('logout/', auth_views.LogoutView.as_view(template_name = 'users/logout.html'),name = 'logout' ),
    path('register/', user_views.register, name = 'register'),
    path ('profile/', user_views.profile, name = 'profile'),
    path("accounts/", include("allauth.urls")),
]

if settings.DEBUG :
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
