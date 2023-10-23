from django.urls import path
from Users import views
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('login/', views.login_request, name="Login"),
    path('signup/', views.register, name='Signup'),
    path('logout/', LogoutView.as_view(template_name='Users/logout.html'), name='Logout'),
    path('edit/', views.editProfile, name='Edit'),
    path('change-password/', views.ChangePassword.as_view(), name='ChangePassword'),
    path('change-password-success/', views.success_password, name='ChangePasswordSuccess'),
]

