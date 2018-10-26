from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    #path('<int:id>/', views.form, name='form'),
    path('', views.homepage, name='homepgae'),
    path('homepage/', views.homepage, name='homepgae'),
    path('logout/', auth_views.LogoutView.as_view(template_name="Forms/logout.htm"), name='logout'),
    path('login/', auth_views.LoginView.as_view(template_name="Forms/login.htm"), name='login'),
    path('passwordChange/', auth_views.PasswordChangeView.as_view(template_name="Forms/changePassword.htm"), name='login'),
    path('doneChangingPass/',auth_views.PasswordChangeDoneView.as_view(template_name='Forms/homepage.htm'), name='password_change_done'),

]