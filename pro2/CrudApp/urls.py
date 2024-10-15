from django.urls import path
from . import views

urlpatterns = [

    path('', views.show),
    path('emp', views.emp),
    path('show', views.show),
    path('edit/<int:id>', views.edit),
    path('delete/<int:id>', views.delete),
    path('update/<int:id>', views.update),


]
