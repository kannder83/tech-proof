from django.urls import path
from . import views


app_name = "proof"

urlpatterns = [
    # ex: /proof/
    path('', views.registers_list, name='registers_list'),
    # ex: /proof/register/1/
    path('register/<int:pk>/', views.register_detail, name='register_detail'),
    # ex: /proof/register/new/
    path('register/new', views.register_new, name='register_new'),
    # ex: /proof/register/1/edit/
    path('register/<int:pk>/edit/', views.register_edit, name='register_edit'),
    # ex: /proof/register/1/delete
    path('register/<int:pk>/delete/',
         views.register_delete, name='register_delete'),
]
