from atexit import register
from . import views
from django.urls import path


urlpatterns = [
    
    path('', views.home, name='home'),
    path('login/', views.login, name='login'),
    path('editprofile/', views.editprofile, name='editprofile'),
    path('changepass/', views.changepass, name='changepass'),
    path('logout/', views.logout, name='logout'),
    path('signup/', views.signup, name='signup'),
    path('set/',views.setcookie),
    path('get/',views.getcookie),
    path('del/',views.delcookie),
    path('set-session/',views.setsession),
    path('get-session/',views.getsession),
    path('del-session/',views.delsession),    
    path('midware/',views.midware),    

]