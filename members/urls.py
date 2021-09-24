from django.urls import path
from . import views

urlpatterns = [
    path('login',views.login_user,name='login'),
    path('logout',views.logout_user,name='logout'),
    path('signup',views.signup_user,name='signup'),
    path('register',views.register,name='register'),
    path('mentors',views.mentors,name='mentors')
]
