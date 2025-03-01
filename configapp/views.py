from django.shortcuts import render,redirect
from configapp.form import StudentsForm,SubjectsForm
from configapp.models import *

def all(request):
    subjects=Subject.objects.all()
    students=Student.objects.all()

    context={
        'subjects':subjects,
        'students':students,
    }
    return render(request,'all.html',context=context)

def subjects(request,subject_id):
    students=Student.objects.filter(subject_id=subject_id)
    subjects=Subject.objects.all()

    context={
        'subjects':subjects,
        'students':students,
    }
    return render(request,'subjects.html',context=context)

def add_subjects(request):
    # print("token = = ",get_token(request)) token tutib olish
    if request.method == "POST":
        form = SubjectsForm(request.POST)
        if form.is_valid():
            subjects = form.save()
            return redirect('home')
    else:
        form = SubjectsForm()
    return render(request,'add_subject.html',{'form':form})

def add_students(request):
    # print("token = = ",get_token(request)) token tutib olish
    if request.method == "POST":
        form = StudentsForm(request.POST)
        if form.is_valid():
            students = form.save()
            return redirect('home')
    else:
        form = StudentsForm()
    return render(request,'add_student.html',{'form':form})
