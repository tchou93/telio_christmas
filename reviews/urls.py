from django.urls import path

from . import views

urlpatterns = [
    path('flux/', views.flux, name='flux'),
    path('posts/', views.posts, name='posts'),
    path('create_ticket/', views.create_ticket, name='create_ticket'),
    path('ticket/delete/<int:pk>', views.delete_ticket, name='delete_ticket'),
    path('ticket/update/<int:pk>', views.update_ticket, name='update_ticket'),
    path('ticket/reserve/<int:pk>', views.reserve_ticket, name='reserve_ticket'),
]
