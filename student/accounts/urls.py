from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.home,name='home'),
    path('signin', views.signin,name='signin'),
    path('signup', views.signup,name='signup'),
    path('forgot', views.forgot,name='forgot'),
    path('department', views.department,name='department'),
    path('gallery', views.gallery,name='gallery'),
    path('contact', views.contact,name='contact'),
    
]