from django.urls import path
from . import views

urlpatterns = [
    path('', views.list_users, name = 'listusers'),
    path('create/', views.create_user, name = 'createuser'),
    path('update/<int:pk>', views.update_user, name = 'uptadeuser'),
    path('delete/<int:pk>', views.delete_user, name = 'deleteuser')
]