from django.urls import path
from django.contrib.auth import views as auth_views
from.import views


app_name = 'socialite'

urlpatterns = [
    path('', views.index, name='index'),
    path('(?P<profile_id>[0-9]+)/', views.indexs, name='comment'),
    path('post-picha', views.ProfileCreateView.as_view(), name = 'post-picha'),
    path('signup', views.signup, name='signup'),
    path('login', views.signin, name='login'),
    path('logout', views.logout, name='logout'),
]