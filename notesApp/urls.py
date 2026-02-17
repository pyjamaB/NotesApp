from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_notes, name='all_notes'),
    path('new_note/', views.create_note, name='create_note'),
    path('<int:pk>/show_note/', views.show_note, name='show_note'),
    path('<int:pk>/edit/', views.edit_note, name='edit_note'),
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('search_notes/', views.search_notes, name='search_notes')
]
