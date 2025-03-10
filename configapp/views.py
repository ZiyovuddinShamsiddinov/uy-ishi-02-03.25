from django.shortcuts import render, redirect, get_object_or_404
from configapp.form import StudentsForm, SubjectsForm
from configapp.models import *
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from reportlab.pdfgen import canvas
from reportlab.lib.utils import ImageReader
from io import BytesIO
import qrcode
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Student, Subject

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

    # Создание буфера для PDF
    buffer = BytesIO()
    p = canvas.Canvas(buffer)

    # Добавляем текст в PDF
    p.drawString(100, 800, f"Название группы: {subject.title}")

    # Генерация QR-кода
    qr_data = f"https://najottalim.uz/?srsltid=AfmBOopzs2E7FZqpvu2Mc-VyPsfGY7UPrFGl30BvUSDnvIBgVmQS6lIR"
    qr = qrcode.make(qr_data)

    # Конвертация QR-кода в формат, который можно вставить в PDF
    qr_buffer = BytesIO()
    qr.save(qr_buffer, format="PNG")
    qr_buffer.seek(0)
    qr_image = ImageReader(qr_buffer)

    p.drawImage(qr_image, 100, 700, width=100, height=100)
    p.showPage()
    p.save()

    buffer.seek(0)
    return HttpResponse(buffer, content_type="application/pdf")


def all(request):
    subjects = Subject.objects.all()
    students = Student.objects.all()

    context = {
        'subjects': subjects,
        'students': students,
    }
    return render(request, 'all.html', context=context)


def subjects(request, subject_id):
    students = Student.objects.filter(subject_id=subject_id)
    subjects = Subject.objects.all()

    context = {
        'subjects': subjects,
        'students': students,
    }
    return render(request, 'subjects.html', context=context)


def add_subjects(request):
    # print("token = = ",get_token(request)) token tutib olish
    if request.method == "POST":
        form = SubjectsForm(request.POST)
        if form.is_valid():
            subjects = form.save()
            return redirect('home')
    else:
        form = SubjectsForm()
    return render(request, 'add_subject.html', {'form': form})


def add_students(request):
    # print("token = = ",get_token(request)) token tutib olish
    if request.method == "POST":
        form = StudentsForm(request.POST)
        if form.is_valid():
            students = form.save()
            return redirect('home')
    else:
        form = StudentsForm()
    return render(request, 'add_student.html', {'form': form})


def update_students(request, subject_id):
    student = get_object_or_404(Student, id=subject_id)
    if request.method == "POST":
        form = StudentsForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = StudentsForm(instance=student)

    return render(request, 'update_student.html', {'form': form, "student": student})


def delete_student(request, subject_id):
    new = get_object_or_404(Student, id=subject_id)
    new.delete()
    return redirect('home')


def student_about(request, subject_id):
    student = get_object_or_404(Student, pk=subject_id)
    context = {
        'student': student,
    }
    return render(request, 'student_about.html', context=context)



# 📌 1. Barcha talabalar ro‘yxati
class StudentListView(ListView):
    model = Student
    template_name = 'all.html'
    context_object_name = 'students'

# 📌 2. Bitta talaba haqida ma'lumot
class StudentDetailView(DetailView):
    model = Student
    template_name = 'student_about.html'
    context_object_name = 'student'

# 📌 3. Talaba qo‘shish
class StudentCreateView(CreateView):
    model = Student
    form_class = StudentsForm
    template_name = 'add_student.html'
    success_url = reverse_lazy('students_list')

# 📌 4. Talabani yangilash
class StudentUpdateView(UpdateView):
    model = Student
    form_class = StudentsForm
    template_name = 'update_student.html'
    success_url = reverse_lazy('students_list')

# 📌 5. Talabani o‘chirish
class StudentDeleteView(DeleteView):
    model = Student
    template_name = 'delete_student.html'
    success_url = reverse_lazy('students_list')

# 📌 6. Fanlar ro‘yxati
class SubjectListView(ListView):
    model = Subject
    template_name = 'subjects.html'
    context_object_name = 'subjects'

# 📌 7. Fan qo‘shish
class SubjectCreateView(CreateView):
    model = Subject
    form_class = SubjectsForm
    template_name = 'add_subject.html'
    success_url = reverse_lazy('subjects_list')