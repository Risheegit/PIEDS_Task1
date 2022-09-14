from django.shortcuts import render, redirect
from .models import Profile
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.views import View

# Create your views here.
def update_user_data(user):
    Profile.objects.update_or_create(user=user, defaults = {'mob': user.profile})

def register(request):
    form_class = UserRegisterForm
    profile_form_class = ProfileUpdateForm
    form = form_class(request.POST or None)
    profile_form = profile_form_class(request.POST or None)
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        profile_form = ProfileUpdateForm(request.POST)
        if form.is_valid() and profile_form.is_valid():
            user = form.save()
            profile = profile_form.save(commit = False)
            if profile.user_id  is None :
                profile.user_id = user.id
            profile.save()
            user.refresh_from_db()
            user.profile.mob = form.cleaned_data.get('mob')
            update_user_data(user)
            user.save()
            messages.success(request, f'Account created for {user.username} !')
            return redirect('login')
            
        else:
            form = UserRegisterForm()
            profile_form = ProfileUpdateForm()
    context = { 'form': form, 'profile_form': profile_form }
    return render(request, 'users/register.html', context)

@login_required
def profile (request):
	if request.method == 'POST':
		#Used to store data that is given 
		u_form = UserUpdateForm(request.POST, instance = request.user)
		p_form = ProfileUpdateForm( request.POST,
								 	request.FILES,
									instance = request.user.profile)
		if u_form.is_valid() and p_form.is_valid():
			u_form.save()
			p_form.save()
			messages.success(request, f'Your account has been updated !')
			return redirect('profile')
		else: 
			print(u_form.errors)
			print(p_form.errors)

	else :
		u_form = UserUpdateForm(instance = request.user)
		p_form = ProfileUpdateForm(instance = request.user.profile)
		
	context = {
		'u_form': u_form,
		'p_form': p_form,
	}
	return render(request, 'users/profile.html', context)

class ProfileView (View):
    def get(self, request, pk, *args, **kwargs):
        profile = Profile.objects.get(pk= pk)
        user = profile.user
        context = {
            'user' : user,
            'profile': profile,
        }

        return render (request, 'users/profile.html', context)