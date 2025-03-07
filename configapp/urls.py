from tkinter.font import names

from django.urls import path
from configapp.views import *
from .views import generate_pdf

urlpatterns = [
    path('all/' , all , name='home'),
    path('subjects/<int:subject_id>', subjects,name='subjects' ),
    path('add_subjects',add_subjects,name='add_subjects'),
    path('add_students', add_students, name='add_students'),
    path('pdf/<int:subject_id>/', generate_pdf, name='generate_pdf'),
    path('qr/najottalim/<int:subject_id>/', generate_qr_najottalim, name='generate_qr_najottalim'),
    path('student_about/<int:subject_id>/', student_about, name='student_about'),
    path('update_students/<int:subject_id>/', update_students, name='update_students'),
    path('delete_student/<int:subject_id>',delete_student,name='delete_student')

]