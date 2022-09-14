from django.urls import path
from users.views import ProfileView, profileupdate

urlpatterns = [
    path('profile/<int:pk>/', ProfileView.as_view(), name = 'profile'),
    path('profile/edit/<int:pk>/', profileupdate , name='profile-edit'),
]