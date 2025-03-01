from django.urls import path
from configapp.views import *

urlpatterns = [
    path('all/' , all , name='home'),
    path('subjects/<int:subject_id>', subjects,name='subjects' ),
    path('add_subjects',add_subjects,name='add_subjects'),
    path('add_students', add_students, name='add_students'),

]