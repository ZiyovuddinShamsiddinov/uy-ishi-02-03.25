from django.urls import path
from configapp.views import *
from .views import generate_pdf

urlpatterns = [
    path('all/' , all , name='home'),
    path('subjects/<int:subject_id>', subjects,name='subjects' ),
    path('add_subjects',add_subjects,name='add_subjects'),
    path('add_students', add_students, name='add_students'),
    path('pdf/<int:subject_id>/', generate_pdf, name='generate_pdf'),
    path('qr/najottalim/', generate_qr_najottalim, name='generate_qr_najottalim'),
]