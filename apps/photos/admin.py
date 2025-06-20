from django.contrib import admin

from apps.photos.models import Photo

@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    list_display = ['pk', 'date_of_publication', 'description', 'get_tagged_pets']

    @staticmethod
    def get_tagged_pets(obj: Photo):
        return ', '.join(pet.name for pet in obj.tagged_pets.all())
