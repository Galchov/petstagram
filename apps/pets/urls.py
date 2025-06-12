from django.urls import include, path
from . import views


urlpatterns = [
    path('add/', views.pet_add_view, name='add-pet'),
    path('<str:username>/pet/<slug:pet_slug>/', include([
        path('', views.pet_details_page_view, name='pet-details'),
        path('edit/', views.pet_edit_view, name='pet-edit'),
        path('delete/', views.pet_delete_view, name='delete-pet'),
    ]))
]
