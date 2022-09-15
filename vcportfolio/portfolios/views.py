from django.shortcuts import render, redirect
from django.views import View
from django.db.models import Q
from django.views.generic import ListView, CreateView, RedirectView
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from .models import Startup
from django.conf import settings
from django.contrib import messages
from django.core.mail import send_mail

# Create your views here.
class StartupListView (ListView):
    model = Startup
    template_name = 'portfolios/home.html'
    context_object_name = 'startups'

#Make a add option if admin 
class StartupCreateView (SuccessMessageMixin,  CreateView):
	model = Startup
	fields = ['startup_name', 'industry', 'logo', 'description', 'website']
	success_url = '/home' 
	success_message = "Your startup was added successfully"
	def get(self, request, *args, **kwargs):
		subject = 'A new company has been added'
		message = f'Hi {request.user.username}, a new company has been added'
		email_from = settings.EMAIL_HOST_USER
		recipient_list = [request.user.email, ]
		send_mail (subject, message, email_from, recipient_list)


class StartupSearch(View):
    def get(self, request, *args, **kwargs):
        query = self.request.GET.get('query')
        startup_list = Startup.objects.filter(
            Q(startup_name__icontains=query)
        )
        context = {
            'startup_list': startup_list,
        }
        return render(request, 'portfolios/startup_search.html', context)

def searchpage (request):
    context = {}
    return render (request, 'portfolios/searchpage.html', context)

def redirect_website (request, website_name):
    return redirect (website_name)

class External_Redirect (RedirectView):
    def post (self, request, *args, **kwargs ):
        # url = request.POST
        print(request.POST['mybtn'])
        website = request.POST['mybtn']
        return redirect (website)

class StartupFilter(View):
    def post (self, request, *args, **kwargs):
        print(request.POST)
        given_industry = request.POST.get('industries', False)
        print("The given industry is ", given_industry)
        filtered_startup = Startup.objects.filter(industry = given_industry)
        context = {
            'filtered_startup':filtered_startup,
        }
        return render (request, 'portfolios/filter_startups.html', context)

def subscribe (request):
    subject = 'Welcome to djvcportfolios'
    message = f'Hi {request.user.username}, thank you registering with us'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [request.user.email, ]
    send_mail (subject, message, email_from, recipient_list)
    messages.success(request, f'Notifications has been enabled !')
    return redirect ('/home/')
