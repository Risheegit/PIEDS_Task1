from django.shortcuts import render, redirect
from django.views import View
from django.db.models import Q
from django.views.generic import ListView, CreateView, RedirectView
from .models import Startup

# Create your views here.
class StartupListView (ListView):
    model = Startup
    template_name = 'portfolios/home.html'
    context_object_name = 'startups'

#Make a add option if admin 
class StartupCreateView ( CreateView):
	model = Startup
	fields = ['startup_name', 'industry', 'logo', 'description']
	success_url = '/home' 

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
        given_industry = request.POST['industry']
        filtered_startup = Startup.objects.filter(industry = given_industry)
        context = {
            'filtered_startup':filtered_startup
        }
        return render (request, 'portfolios/filter_startups.html', context)