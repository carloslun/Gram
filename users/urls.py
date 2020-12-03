from django.urls import path, include
from django.views.generic import TemplateView
from users import views 

urlpatterns = [
    # posts
    path(
        route = 'profile/<str:username>/',
        # view = TemplateView.as_view(template_name = 'users/detail.html'),
        view = views.UserDetailView.as_view(),
        name = 'detail'
    ),
    
    path(
        route ='login/', 
        view = views.LoginView.as_view(), 
        name ='login'
        ),
    path( 
        route ='logout/', 
        view = views.LogoutView.as_view(), 
        name = 'logout'
        ),
    path(
        route ='signup/', 
        view = views.SignupFormView.as_view(), 
        name = 'signup'
        ),
    path(
        route ='me/profile/', 
        view = views.ProfileUpdateView.as_view(), 
        name = 'update_profile'
        ),
    
]