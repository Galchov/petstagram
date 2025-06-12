from django.urls import path, include
from . import views


urlpatterns = [
    path('add/', views.photo_add_page_view, name='add-photo'),
    path('<int:pk>/', include([
        path('', views.photo_details_page_view, name='photo-details'),
        path('edit/', views.photo_edit_page_view, name='photo-edit'),
    ]))
]
