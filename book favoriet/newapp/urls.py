from django.urls import path     
from . import views

urlpatterns = [
    path('', views.index),
    path('reglog', views.reglog),
    path('welcome', views.welcome),
    path('logout', views.logout),
    path('add_book', views.add_book),
    path('show_books/<int:id>', views.show_books),
    path('add_to_fav/<int:id>', views.add_to_fav),
    path('edit/<int:id>', views.edit),
    path('delete/<int:id>', views.delete),
    path('breack_up/<int:id>', views.breack_up),
]
