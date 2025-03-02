from io import BytesIO
from reportlab.pdfgen import canvas
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from configapp.form import StudentsForm,SubjectsForm
from configapp.models import *
import qrcode

def generate_qr_najottalim(request):
    url = "https://najottalim.uz/"
    qr = qrcode.make(url)

    buffer = BytesIO()
    qr.save(buffer, format="PNG")
    buffer.seek(0)

    return HttpResponse(buffer.getvalue(), content_type="image/png")

url = "https://example.com/group/123"  # Ссылка на группу
qr = qrcode.make(url)
qr.save("qrcode.png")  # Сохранение QR-кода


def generate_pdf(request, subject_id):
    subject = get_object_or_404(Subject, id=subject_id)
    buffer = BytesIO()
    p = canvas.Canvas(buffer)  # canvas теперь импортирован правильно
    p.drawString(100, 800, f"Название группы: {subject.title}")
    p.showPage()
    p.save()

    buffer.seek(0)
    return HttpResponse(buffer, content_type="application/pdf")

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
