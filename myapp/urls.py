from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name= 'index'),
    path('index.html', views.index, name= 'index'),
    path('random',views.random, name='random'),
    path('users-profile', views.profile,name='users-profile' ),
    path('plagerism.html',views.plagerism,name='plagerism'),
    path('teaching.html',views.teaching,name='teaching'),
    path('users-profile.html',views.profile,name='user-profile'),
    path('my_function/', views.my_function, name='my_function'),
    path('performance.html',views.performance,name='performance'),
    path('MU.html',views.plagerism,name='MU'),
    path('Attendence.html',views.attend,name='Attendence'),
    path('Feedback.html',views.feedback,name='feedback'),
    path('Assignments.html',views.feedback,name='assignment'),
    path('pages-login.html',views.feedback,name='login')

]