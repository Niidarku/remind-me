from django.urls import path
from .import views

#create urls paths here
app_name= 'todois'


urlpatterns = [
    path('register/', views.register, name='registration'),
    # path('login/',views.login,name='login'),
    # path('users/', views.users, name='users_page')
]