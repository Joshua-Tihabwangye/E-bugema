from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.RegisterView.as_view(), name='register'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('refresh/', views.RefreshView.as_view(), name='token_refresh'),
    path('me/', views.me, name='me'),
    path('profile/', views.update_profile, name='update_profile'),
    path('logout/', views.logout, name='logout'),
    
    # Admin routes
    path('users/', views.AdminUserListView.as_view(), name='admin_user_list'),
    path('users/<uuid:user_id>/role/', views.admin_update_user_role, name='admin_update_user_role'),
    path('users/<uuid:user_id>/', views.admin_delete_user, name='admin_delete_user'),
]
