from django.urls import path
from libary import views

app_name = 'libary'

urlpatterns = [
    path('', views.index, name='index'),
    path('search/', views.search, name='search'),

    # CRUD - BOOK
    path('book/<int:book_id>/', views.book, name='book'),
    path('book/create/', views.create, name='create'),
    path('book/<int:book_id>/update/', views.update, name='update'),
    path('book/<int:book_id>/delete/', views.delete, name='delete'),

    # CRUD - USER
    path('user/', views.user_read, name='user_read'),
    path('user/register/', views.register, name='register'),
    path('user/login/', views.login_view, name='login'),
    path('user/logout/', views.logout_view, name='logout'),
    path('user/update/', views.user_update, name='user_update'),

]
