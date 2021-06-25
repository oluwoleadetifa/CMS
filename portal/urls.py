from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [path('', views.IndexView, name='portal.index'),
               path('login/', views.Login, name='portal.login'),
               path('logout/', views.logoutUser, name='portal.logout'),
               # Forget Password
               path('password-reset/',
                    auth_views.PasswordResetView.as_view(
                        template_name='portal/password_reset/password_reset_form.html',
                        subject_template_name='portal/password_reset/password_reset_subject.txt',
                        email_template_name='portal/password_reset/password_reset_email.html',
                        # success_url='/login/'
                    ),
                    name='password_reset'),
               path('password-reset/done/',
                    auth_views.PasswordResetDoneView.as_view(
                        template_name='portal/password_reset/password_reset_done.html'
                    ),
                    name='password_reset_done'),
               path('password-reset-confirm/<slug:uidb64>/<slug:token>/',
                    auth_views.PasswordResetConfirmView.as_view(
                        template_name='portal/password_reset/password_reset_confirm.html'
                    ),
                    name='password_reset_confirm'),
               path('password-reset-complete/',
                    auth_views.PasswordResetCompleteView.as_view(
                        template_name='portal/password_reset/password_reset_complete.html'
                    ),
                    name='password_reset_complete'),
               ]
