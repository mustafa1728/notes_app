from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('add', views.add_note_editor, name = 'add_note_editor'), 
    path('delete/<note_id>', views.deleteNote, name = 'delete'),
    path('edit/<note_id>', views.editNote, name = 'edit_note_editor')
]
