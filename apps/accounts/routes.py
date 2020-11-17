from django.urls import path

from knox import views as knox_views

from apps.accounts.viewsets import LoginView

app_name = 'accounts'

url_patterns = [
    # Authentication Routes.
    path('login', LoginView.as_view(), name='login'),
    path('logout', knox_views.LogoutView.as_view(), name='logout'),
    path('logoutall', knox_views.LogoutAllView.as_view(), name='logoutall')
]
