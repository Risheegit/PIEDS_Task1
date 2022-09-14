from django import forms
from .models import Startup

# creating a form
class StartupCreateForm(forms.ModelForm):
	class Meta :
		model = Startup
		fields =  ['startup_name', 'description', 'industry', 'logo', 'website']
