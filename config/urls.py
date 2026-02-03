"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.contrib.auth.views import LogoutView
from user import views
from user.views import (CustomLoginView, signup, ForgotPasswordView, VerifyOTPView, ResetPasswordView)

csrf_failure_view = "user.views.csrf_failure"
handler400 = 'user.views.error_400'
handler403 = 'user.views.error_403'
handler404 = 'user.views.error_404'
handler500 = 'user.views.error_500'

urlpatterns = [
    path('', views.home, name='home'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('signup/', signup, name='signup'),
    path('logout/', LogoutView.as_view(next_page='home'), name='logout'),
    path('forgot-password/', ForgotPasswordView.as_view(), name='forgot_password'),
    path('resend-otp/', views.ResendOTPView.as_view(), name='resend_otp'),
    path('verify-otp/', VerifyOTPView.as_view(), name='verify_otp'),
    path('reset-password/', ResetPasswordView.as_view(), name='reset_password'),
    path('admin/', admin.site.urls),
    path('profile/', views.profile_view, name='profile'),
    path('toggle-language/', views.toggle_language, name='toggle_language'),
    path('export-data/', views.export_user_data, name='export_data'),
    path('delete-account/', views.delete_account, name='delete_account'),
    path('privacy-audit/', views.privacy_audit_report, name='privacy_audit'),
    path('privacy-policy/', views.privacy_policy, name='privacy_policy'),
    path('privacy-audit/download/', views.download_privacy_audit, name='download_audit_pdf'),
    path('freeze-profile/', views.freeze_profile, name='freeze_profile'),
    path('request-edit/', views.request_edit, name='request_edit'),
    path('manager-dashboard/', views.manager_dashboard, name='manager_dashboard'),
    path('action/<int:user_id>/<str:action>/', views.manage_user_action, name='manage_user_action'),
    path('captcha/', include('captcha.urls')),
]