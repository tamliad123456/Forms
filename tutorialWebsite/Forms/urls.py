from django.urls import path
from . import views

urlpatterns = [
    #path('<int:id>/', views.form, name='form'),
    path('', views.homepage, name='homepgae'),
    path('homepage/', views.homepage, name='homepgae'),
    path('login/', views.login, name='login')
]